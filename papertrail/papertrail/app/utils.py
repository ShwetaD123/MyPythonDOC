from flask import flash
import boto3, botocore
from papertrail.config import BaseConfig
from bson import json_util
import json


s3 = boto3.client("s3")

def upload_file_to_s3(file, bucket_name=BaseConfig.AWS_S3_BUCKET, acl="public-read"):

    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename
        )
        s3_obj_url = "{}{}".format(BaseConfig.AWS_S3_LOCATION, file.filename)

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return s3_obj_url




def get_obj_list():

    s3 = boto3.resource('s3')

    bucket = s3.Bucket(BaseConfig.AWS_S3_BUCKET)
    objlst = [(x.key, x.last_modified) for x in bucket.objects.all()]
    return json.dumps(objlst, default=json_util.default)



def last(n):
    m = 2
    return n[m]

def sort(tuples):
    SortedOP=sorted(tuples, key=last)
    # print("SortedOP===>",SortedOP)
    return sorted(tuples, key=last)

bucket = boto3.client("s3")



dynamodb = boto3.resource('dynamodb',
                          region_name = "us-east-1")


import uuid

def storeToDb(D1,tableName):
    print("D1  ================= > ",D1)
    D1['id'] = uuid.uuid4().hex
    print("----------",D1['id'])
    client = boto3.resource('dynamodb',
                            region_name = "us-east-1")

    table = client.Table(tableName)
    Dict=D1
    print(D1)
    print ("Dict===>",Dict)

    return table.put_item(Item=D1)


def getListfilenames(filenames,options):

    return list(zip(filenames, options))




def storeDbBulkData(ComboDict,BulkUpload):
    client = boto3.resource('dynamodb',
                            region_name="us-east-1")
    table = client.Table(BulkUpload)

    for i in ComboDict:
        print("SingleDIct ------",i)
        i['FileName'] = i.pop('0')
        i['ImageUrl'] = i.pop('1')
        i['Option'] = i.pop('2')
        # i.rename('1','ImageUrl')
        # i.rename("2","Option")
        i.update({'id': uuid.uuid4().hex})
        i.update({'BucketName':BaseConfig.AWS_S3_BUCKET})
        print("NewDict --------",i)
        table.put_item(Item=i)


    return ("Data Stored Successfully ------------------!!!")



def Convert(ListOfFileAndOptions, dictOfBulkOption) :
    objUrl=[]
    for a, b in ListOfFileAndOptions:
        dictOfBulkOption.setdefault(a, []).append(b)
        objUrl.append("https://{0}.s3.amazonaws.com/{1}".format(BaseConfig.AWS_S3_BUCKET, ListOfFileAndOptions[0][0]))
    print("objUrl === ",objUrl)

    return dictOfBulkOption,objUrl

#
#
#
#
# def get_BulkObj_list():
#
#     s3 = boto3.resource('s3')
#
#     bucket = s3.Bucket(BaseConfig.AWS_S3_BUCKET_BULK)
#     objlst = [(x.key, x.last_modified) for x in bucket.objects.all()]
#     return json.dumps(objlst, default=json_util.default)
#
#
# def storeBulkOptToDb(dict1,OrgDict):
#     OrgDict = {}
#     for k,v in dict1. :
#         print()


def getFinalList(filenames,ListofOptions,UrlList):
    p = map(list, zip(*[filenames, ListofOptions, UrlList]))
    print(p)
    W = []
    for i in p:
        print(i)
        D = {str(k): v for k, v in enumerate(i)}
        W.append(D)
    return W


import os
import boto3



def multiupload():
    s3 = boto3.resource('s3')

    directory_in_str = "/home/ubantu/Documents/PROJECT/papertrail/uploads"  # change directory path to your images folder
    # print("directory_in_str ----->", directory_in_str)

    directory = os.fsencode(directory_in_str)
    # print("directory ==========>", directory)

    for file in os.listdir(directory):
        print("file ---->", file)
        filename = os.fsdecode(file)
        if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):

            strg = directory_in_str + '/' + filename
            # print("strg  ---------->", strg)
            file = open(strg, 'rb')
            # print("FileTORead ------------>", file)
            object = s3.Object(BaseConfig.AWS_S3_BUCKET, filename)
            object.put(Body=file, ContentType='')

        else:
            continue

    list1 = [filename for filename in os.listdir('/home/ubantu/Documents/PROJECT/papertrail/uploads') if
             filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png")]
    print(list1)
    for f in list1:
        os.remove("/home/ubantu/Documents/PROJECT/papertrail/uploads/{}".format(f))

    flash("File Uploaded Successfully")

def get_obj_Bulklist():

    s3 = boto3.resource('s3')

    bucket = s3.Bucket(BaseConfig.AWS_S3_BUCKET)
    objlst = [(x.key, x.last_modified) for x in bucket.objects.all()]
    print(objlst)
    result =json.dumps(objlst, default=json_util.default)
    print("result of bulkList ------- >",result)
    return result
