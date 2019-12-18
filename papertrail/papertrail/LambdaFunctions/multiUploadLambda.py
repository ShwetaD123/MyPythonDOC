import json
import uuid
from PIL import Image, ImageEnhance
import boto3
import re
from datetime import datetime

s3_client = boto3.client("s3")


def grayscale(download_path, upload_path):
    colorImage = Image.open(download_path)
    key = colorImage.convert('L')  # conversion to gray scale
    key.save(upload_path, dpi=(300, 300))


def binary(download_path, upload_path):
    colorImage = Image.open(download_path)
    key = colorImage.convert('1')  # conversion to gray scale
    key.save(upload_path, dpi=(300, 300))


def contrast(download_path, upload_path):
    colorImage = Image.open(download_path)
    enhancer = ImageEnhance.Contrast(colorImage)
    key = enhancer.enhance(3.0)
    key.save(upload_path, dpi=(300, 300))


def sharpness(download_path, upload_path):
    colorImage = Image.open(download_path)
    enhancer = ImageEnhance.Sharpness(colorImage.convert('RGB'))
    key = enhancer.enhance(3.0)
    key.save(upload_path, dpi=(300, 300))


def original(download_path, upload_path):
    colorImage = Image.open(download_path)
    enhancer = ImageEnhance.Sharpness(colorImage)
    key = enhancer.enhance(1.0)
    key.save(upload_path, dpi=(300, 300))


def get_ListOfDict(event):
    ListOfDict = []

    for item in event["Records"]:
        if "OldImage" in item['dynamodb'].keys():
            MainDict = (item['dynamodb']['OldImage'])
        else:
            MainDict = (item['dynamodb']['NewImage'])

        keys = []
        val = []
        for i in MainDict:
            keys.append(i)
            val.append(MainDict[i]['S'])
        newDict = dict(zip(keys, val))

        print("NewDict ===", newDict)
        ListOfDict.append(newDict)

    print("ListOfDict ------------", ListOfDict)

    return (ListOfDict)


def processingOption(option, ConvBucket, key1, download_path, upload_path):
    if option == "sharpness":
        sharpness(download_path, upload_path)


    elif option == "contrast":
        contrast(download_path, upload_path)

    elif option == "grayscale":
        print("UploadPath ---->", upload_path)
        print("download_path ---->", download_path)
        grayscale(download_path, upload_path)


    elif option == "binary":
        binary(download_path, upload_path)


    elif option == "original":
        original(download_path, upload_path)

    s3_client.upload_file(upload_path, '{}'.format(ConvBucket), key1)
    return ("Image Converted and Processed Successfully")


def download_and_upload(result):
    for newDict in result:
        key = newDict["FileName"]
        bucket = newDict["BucketName"]
        option = newDict['Option']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        print("download_path ------", download_path)

        upload_path = '/tmp/{}'.format(key)
        print("UploadPath ------", upload_path)

        key1 = option + "_" + key

        print(key1)
        s3_client.download_file(bucket, key, download_path)
        print("-----------File Uploaded successfully ----------")
        ConvBucket = "surveyprojecttestbinary"
        processingOption(option, ConvBucket, key1, download_path, upload_path)
        print("IMage converted and UPloaded successfully")
        print("-----------Calling function for Textract processing ----------")
        textractvalues = extractKeyAndValuePair(ConvBucket, key1, bucket, key)


def lambda_handler(event, context):
    print("event====>", event)
    result = get_ListOfDict(event)
    print("Result ----", result)
    Rec = download_and_upload(result)
    print("REcord ----", Rec)

    return {

        'statusCode': 200,
        'body': json.dumps('Welcome to lambda process AWS Function')
    }


def extractKeyAndValuePair(ConvBucket, key1, bucket, key):
    print("===Textract Functionality is start===")
    client = boto3.client('textract')
    key_map, value_map, block_map = get_kv_map(ConvBucket, key1)
    kvs = get_kv_relationship(key_map, value_map, block_map)
    print("\n\n== FOUND KEY : VALUE pairs ===\n")
    print_kvs(kvs)
    result = get_kv_relationship_confidence(key_map, value_map, block_map)
    print("confidence_score==>", result)
    client = boto3.resource('dynamodb')
    table = client.Table("InfoTable")
    data = update_to_dynamodb(kvs)
    object_url = "https://{0}.s3.amazonaws.com/{1}".format(ConvBucket, key1)
    Originalobject_url = "https://{0}.s3.amazonaws.com/{1}".format(bucket, key)
    data['Confidence_score'] = result
    data['ImageName'] = key1
    data['ImageLink'] = object_url
    data['Image Preprocessing'] = "Grayscale,Binary,Sharpness,Contrast"
    data['OriginalImageLink'] = Originalobject_url
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['UploadTime'] = current_time
    table.put_item(Item=data)
    return ("----------------- Data stored and key value pairs extracted successfully-------------")


#


def get_kv_map(bucket, key):
    client = boto3.client('textract')
    response = client.analyze_document(
        Document={'S3Object': {'Bucket': bucket, 'Name': key}}, FeatureTypes=["FORMS"])

    # Get the text blocks
    blocks = response['Blocks']
    key_map = {}
    value_map = {}
    block_map = {}
    for block in blocks:
        block_id = block['Id']
        block_map[block_id] = block
        if block['BlockType'] == "KEY_VALUE_SET":
            if 'KEY' in block['EntityTypes']:
                key_map[block_id] = block
            else:
                value_map[block_id] = block
    return key_map, value_map, block_map


def get_kv_relationship(key_map, value_map, block_map):
    kvs = {}
    for block_id, key_block in key_map.items():
        value_block = find_value_block(key_block, value_map)
        key = get_text(key_block, block_map)
        val = get_text(value_block, block_map)
        kvs[key] = val
    return kvs


def get_kv_relationship_confidence(key_map, value_map, block_map):
    kvs = {}
    for block_id, key_block in key_map.items():
        value_block = find_value_block(key_block, value_map)
        key = get_text_confidence(key_block, block_map)
        val = get_text_confidence(value_block, block_map)
        kvs[key] = val
    result = get_confidence_score(kvs)
    print("resultConScore===>", result)
    return result


def get_text_confidence(result, blocks_map):
    text = ''
    confidence_Map = []
    if 'Relationships' in result:
        for relationship in result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    word = blocks_map[child_id]
                    confidence_Map.append(word['Confidence'])

                    if word['BlockType'] == 'WORD':
                        text += word['Text'] + ' '
                    if word['BlockType'] == 'SELECTION_ELEMENT':
                        if word['SelectionStatus'] == 'SELECTED':
                            text += 'X '

    try:
        confidence_score = sum(confidence_Map) / len(confidence_Map)
    except ZeroDivisionError:
        return (0, "Null")
    print("text====>", text, "confidence_score====>", confidence_score)
    return text, confidence_score


def get_confidence_score(kvs):
    list1 = []

    for k, v in kvs.items():
        if k[1] != 'Null' and v[1] != 'Null':
            list1.append(k[1] + v[1])

    N = len(list1) * 2
    if N != list1 != 0:
        try:
            RESULT = sum(list1) / N
            confidence_score = round(RESULT)
        except:
            confidence_score = "No result extracted"

    return confidence_score


def find_value_block(key_block, value_map):
    for relationship in key_block['Relationships']:
        if relationship['Type'] == 'VALUE':
            for value_id in relationship['Ids']:
                value_block = value_map[value_id]
    return value_block


def get_text(result, blocks_map):
    text = ''
    if 'Relationships' in result:
        for relationship in result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    word = blocks_map[child_id]
                    if word['BlockType'] == 'WORD':
                        text += word['Text'] + ' '
                    if word['BlockType'] == 'SELECTION_ELEMENT':
                        if word['SelectionStatus'] == 'SELECTED':
                            text += 'X '
    return text


def print_kvs(kvs):
    for key, value in kvs.items():
        print(key, ":", value)
    print(kvs)


def search_value(kvs, search_key):
    for key, value in kvs.items():
        if re.search(search_key, key, re.IGNORECASE):
            return value


def update_to_dynamodb(kvs):
    fdic = {}
    for item, value in kvs.items():
        if kvs[item] and item != '':
            fdic[item] = value

    fdic['RecId'] = uuid.uuid4().hex
    return (fdic)





