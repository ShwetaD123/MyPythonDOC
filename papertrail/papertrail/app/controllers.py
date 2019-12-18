import uuid
from multiprocessing import Pool
import boto3
import os, json
from flask import Blueprint,render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from papertrail.config import BaseConfig
from papertrail.app.utils import upload_file_to_s3, get_obj_list,sort,dynamodb,storeToDb,multiupload,get_obj_Bulklist,Convert,storeDbBulkData,getFinalList
from datetime import datetime
from datetime import date




def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in BaseConfig.ALLOWED_EXTENSIONS


papp = Blueprint('papp', __name__, template_folder='templates')


@papp.route('')
# @cache.cached(300)
def app_home():
    return render_template('app_home.htm')



@papp.route('/upload', methods=['GET', 'POST'])
# @cache.cached(300)
def app_upload():
    if request.method == 'POST':
        print(request)
        print(request.form.getlist('options'))
        OptionList=request.form.getlist('options')
        print("Inside post method")
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            output = upload_file_to_s3(file, BaseConfig.AWS_S3_BUCKET)
            print(str(output))
            print(OptionList)
            D1 = {str(k): v for k, v in enumerate(OptionList)}
            D1['Filename'] = file.filename
            D1['BucketName'] = BaseConfig.AWS_S3_BUCKET
            database = storeToDb(D1,'data')

            flash('File Uploaded successfully')
            # file.save(os.path.join(BaseConfig.UPLOAD_FOLDER, file.filename))

            return redirect(url_for('papp.app_upload',
                                    filename=file.filename,message="File Uploaded successfully"))

    return render_template('app_upload.htm')


@papp.route('/geturl+lobject', methods=['GET'])
def get_url_objects():
    oblst = json.loads(get_obj_list())
    oblst = [[x[0], x[1]["$date"] / 1000] for x in oblst]
    oblst = [(x[0], datetime.utcfromtimestamp(x[1]).strftime('%H:%M:%S')) for x in oblst]
    bucket = boto3.client("s3")
    mainlist = []
    for key in oblst:
        listurl = []
        object_url = "https://{0}.s3.amazonaws.com/{1}".format(BaseConfig.AWS_S3_BUCKET, key[0])
        listurl.append(object_url)
        listurl.extend(key)
        today = date.today()
        uploadedDate=today.strftime("%d/%m/%Y")
        listurl.append(uploadedDate)
        mainlist.append(tuple(listurl))
        mainlist=sort(mainlist)
    print("mainlistList======>",mainlist)
    return render_template('objectlist.html', files=mainlist[::-1])





@papp.route('/allDbRec', methods=['GET'])
def textRecord():
    table = dynamodb.Table('InfoTable')
    rec = table.scan()
    print(rec)
    return render_template('textRec.html', data=rec)



@papp.route('/upload/bulk')
# @cache.cached(300)
def app_upload_bulk():
   return render_template('app_upload_bulk.htm')



@papp.route('/bulk', methods=['GET', 'POST'])
def bulk():
   if request.method == 'POST':
       uploaded_files = request.files.getlist("file[]")
       print('------', uploaded_files)
       options = request.form.getlist("options")
       print("List of Options ----- ", options)
       if uploaded_files == [ ]:
           flash('No selected file')
           return redirect(request.url)

       filenames = []
       for file in uploaded_files:
           if file and allowed_file(file.filename):
               filename = secure_filename(file.filename)
               file.save(os.path.join(BaseConfig.UPLOAD_FOLDER, filename))
               filenames.append(filename)
       print("filenames-------->", filenames)
       urlList = []
       for i in filenames:
           urlList.append("https://{0}.s3.amazonaws.com/{1}".format(BaseConfig.AWS_S3_BUCKET, i))

       print("UrlList ------", urlList)
       ComboDict = getFinalList(filenames, urlList, options)
       print("DICTIONARY ***  ", ComboDict)
       res = storeDbBulkData(ComboDict, 'BulkUpload')
       print(res)

       result = multiupload()
       print("result----****", result)


   return render_template('app_upload_bulk.htm')







# @papp.route('/bulkObjList', methods=['GET'])
# # @cache.cached(300)
# def listOf_bulk_Object():
#     oblst = json.loads(get_obj_Bulklist())
#     oblst = [[x[0], x[1]["$date"] / 1000] for x in oblst]
#     oblst = [(x[0], datetime.utcfromtimestamp(x[1]).strftime('%H:%M:%S')) for x in oblst]
#     print("****** ----- >",oblst)
#     BulkList = []
#     for key in oblst:
#         listurl = []
#         object_url = "https://{0}.s3.amazonaws.com/{1}".format(BaseConfig.AWS_S3_BUCKET, key[0])
#         listurl.append(object_url)
#         listurl.extend(key)
#         today = date.today()
#         uploadedDate=today.strftime("%d/%m/%Y")
#         listurl.append(uploadedDate)
#         BulkList.append(tuple(listurl))
#         BulkList=sort(BulkList)
#     print("BulkList======>",BulkList)
#     return render_template('bulkList.html', files=BulkList[::-1])









@papp.route('/getImage/<id>', methods=['GET'])
def getById(id):
    print(id)
    client = boto3.client(
        'dynamodb',
        region_name="us-east-1")


    rec = client.get_item(
        TableName='InfoTable',
        Key={
            'RecId': {'S':str(id)}
        }
    )
    del(rec['Item']['Confidence_score'])
    print("rec=====>",rec)
    return render_template('recordByRecId.html',data=rec)


#
# @papp.route('/bulkDbRec', methods=['GET'])
# def bulkTextRecord():
#     table = dynamodb.Table('OutputTable')
#     rec = table.scan()
#     print("bULK record --------------",rec)
#     return render_template('bulkTextRec.html', data=rec)



#
# @papp.route('/Image/<id>', methods=['GET'])
# def ById(id):
#     print(id)
#     client = boto3.client(
#         'dynamodb',
#         region_name="us-east-1")
#
#
#     rec = client.get_item(
#         TableName='OutputTable',
#         Key={
#             'RecId': {'S':str(id)}
#         }
#     )
#     del(rec['Item']['Confidence_score'])
#     print("rec=====>",rec)
#     return render_template('records.html',data=rec)
