from flask import Flask, render_template, request, jsonify, redirect
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'

print('hello world')


@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        getAll_sql = 'SELECT * FROM studentDetails'
        cursor = db_conn.cursor()
        cursor.execute(getAll_sql)
        results = cursor.fetchall()
        print(results)
    except Exception as e:
        return render_template('error.html', error_msg=str(e))

    return render_template('adminDashboard.html', studentList = results)

@app.route("/addStudent", methods=['GET'])
def renderAddStudent():
    return render_template('addStudent.html')

@app.route("/editStudent", methods=['GET'])
def renderEditStudent():
    student_id = request.args['student_id']
    student_name = request.args['student_name']
    student_nric = request.args['student_nric']
    student_gender = request.args['student_gender']
    student_programme = request.args['student_programme']
    student_email = request.args['student_email']
    student_mobile = request.args['mobile_number']

    rowData = [student_id, student_name, student_nric, student_gender, student_programme, student_email,student_mobile]
    
    pdf_url = "https://{0}.s3.amazonaws.com/{1}.pdf".format(custombucket,student_id)
    image_url = "https://{0}.s3.amazonaws.com/{1}.png".format(custombucket,student_id)

    return render_template('editStudent.html', data=rowData,image_url =image_url, report_url=pdf_url)

@app.route("/deleteStudent", methods=['POST'])
def deleteStudent():
    student_id = request.form['student_id']
    delete_sql = "DELETE FROM studentDetails WHERE student_id = %s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(delete_sql, student_id)
        db_conn.commit()
        print("Successfully Deleted From Database")
        cursor.close()
        return redirect("/")
    except Exception as e:
        cursor.close()
        return render_template('error.html', error_msg='Unable to Delete From MariaDB')



@app.route("/editStudent", methods = ['POST'])
def updateStudent():
    student_id = request.form['student_id']
    student_name = request.form['student_name']
    student_nric = request.form['student_nric']
    student_gender = request.form['student_gender']
    student_programme = request.form['student_programme']
    student_email = request.form['student_email']
    student_mobile = request.form['mobile_number']

    update_sql = "UPDATE studentDetails SET student_name = %s, student_nric = %s, student_gender = %s, student_programme = %s, student_email = %s, mobile_number = %s WHERE student_id = %s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(update_sql, (student_name, student_nric, student_gender, student_programme,student_email, student_mobile, student_id))
        db_conn.commit()
        print("Successfully Updated the Database")
        cursor.close()
        return redirect('/')
    except Exception as e:
        cursor.close()
        return render_template('error.html', error_msg='Unable to Update into MariaDB')

@app.route("/getStudentDetails", methods=['GET'])
def getStudent():
    student_id = request.args.get('student_id')
    get_sql = 'SELECT * FROM studentDetails WHERE student_id = %s'
    cursor = db_conn.cursor()
    cursor.execute(get_sql, student_id)
    results = cursor.fetchone()

    pdf_url = "https://{0}.s3.amazonaws.com/{1}.pdf".format(custombucket,student_id)
    image_url = "https://{0}.s3.amazonaws.com/{1}.png".format(custombucket,student_id)

    return render_template('studentDetails.html', data=results,image_url =image_url, report_url=pdf_url)


@app.route("/addStudent", methods=['POST'])
def addStudent():

    student_id = request.form['student_id']
    progress_report = request.files['progress_report']

    print(progress_report.content_type)

    # Validation to ensure there is no empty file
    if progress_report.filename == '':
        return 'Please Insert A File'

    file_extension = getFileExtension(progress_report.filename)
    print(file_extension)

    insertSuccess = insertIntoMariaDB(request)

    if insertSuccess is False:
        return render_template('error.html', error_msg='Unable to insert into MariaDB')

    print('Done Inserting into MariaDB, now Uploading to S3')

    if isEc2Instance is False:
        print("Local Development Environment, Skipping Uploading to S3")
    else:
        uploadSuccess = uploadPDF(progress_report, student_id)
        if uploadSuccess is False:
            return render_template('error.html', error_msg='There is problem with S3, Please SSH Into your Instances to Check it Out')

    return redirect('/')

def getFileExtension(file):
    return os.path.splitext(file)[1]

def uploadImage(image_to_upload, student_id):
    print("Uploading Image Into S3 Bucket")
    file_extension = getFileExtension(image_to_upload.filename)
    file_name = student_id + file_extension
    return uploadToS3(file_name, image_to_upload)

def uploadPDF(pdf_to_upload, student_id):
    print("Uploading PDF into S3 Bucket")
    file_extension = getFileExtension(pdf_to_upload.filename)
    file_name = student_id + file_extension
    return uploadToS3(file_name, pdf_to_upload)

def uploadToS3(file_name, file_content):

    try:
        s3 = boto3.resource('s3')
        s3.Bucket(custombucket).put_object(Key=file_name, Body=file_content)
        bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
        s3_location = (bucket_location['LocationConstraint'])

        if s3_location is None:
            s3_location = ''
        else:
            s3_location = '-' + s3_location

        object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
            s3_location,
            custombucket,
            file_name)

        print(f'Success, Uploaded File Object URL {object_url}')
        return True
    except Exception as e:
        print(str(e))
        return False

def insertIntoMariaDB(request):
    print("Updating Database for Maria DB")
    student_id = request.form['student_id']
    student_name = request.form['student_name']
    student_nric = request.form['student_nric']
    student_gender = request.form['student_gender']
    student_programme = request.form['student_programme']
    student_email = request.form['student_email']
    student_mobile = request.form['mobile_number']

    insert_sql = "INSERT INTO studentDetails VALUES(%s, %s, %s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:
        cursor.execute(insert_sql, (student_id, student_name, student_nric, student_gender, student_programme,student_email, student_mobile))
        db_conn.commit()
        print("Successfully Uploading into Database")
        cursor.close()
        return True

    except Exception as e:
        cursor.close()
        print(str(e))
        return False


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.tarc.edu.my')


@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    location = request.form['location']
    emp_image_file = request.files['emp_image_file']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"

    try:

        cursor.execute(insert_sql, (emp_id, first_name, last_name, pri_skill, location))
        db_conn.commit()
        emp_name = "" + first_name + " " + last_name
        # Uplaod image file in S3 #
        emp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file" + ".png"
        s3 = boto3.resource('s3')

        try:
            print("Data inserted in MySQL RDS... uploading image to S3...")
            s3.Bucket(custombucket).put_object(Key=emp_image_file_name_in_s3, Body=emp_image_file)
            bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
            s3_location = (bucket_location['LocationConstraint'])

            if s3_location is None:
                s3_location = ''
            else:
                s3_location = '-' + s3_location

            object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                s3_location,
                custombucket,
                emp_image_file_name_in_s3)

        except Exception as e:
            return str(e)

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=emp_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

