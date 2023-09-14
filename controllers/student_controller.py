from datetime import date, datetime, time
from flask import Blueprint, redirect, render_template, request, session

from config import *
from models import student_model
from services.database_service import get_database_connection
from services.s3_service import uploadToS3, getProgressionReports
from functools import wraps

student_controller = Blueprint('student_controller,', __name__)

#Session Validation wihwrapper
def require_session(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if 'student_id' not in session:
            return redirect('/')  # Redirect to the home page if no session is found
        return view_function(*args, **kwargs)
    return decorated_function

@student_controller.route('/register', methods=['GET'])
def render_register():
    return render_template('addStudent.html')


@student_controller.route('/dashboard', methods=['GET'])
@require_session
def dashboard():
    student_id = session['student_id']
    image_url = "https://{0}.s3.amazonaws.com/students/{1}/profile.png".format(custombucket,student_id)
    return render_template('student/studentDashboard.html', image_url=image_url)

@student_controller.route('/search', methods=['GET'])
@require_session
def search_internship():
    student_id = session['student_id']
    image_url = "https://{0}.s3.amazonaws.com/students/{1}/profile.png".format(custombucket,student_id)
    #Fetch All Internship Offers


    return render_template('student/internship.html', data=[], image_url=image_url)

@student_controller.route('/profile', methods=['GET'])
@require_session
def profile():
    student_id = session['student_id']
    print("student id: ", student_id)
    results = student_model.get_student(student_id)
    pdf_url = "https://{0}.s3.amazonaws.com/{1}.pdf".format(custombucket,student_id)
    student_id = session['student_id']
    image_url = "https://{0}.s3.amazonaws.com/students/{1}/profile.png".format(custombucket,student_id)
    print(image_url)
    return render_template('student/profile.html', data=results,image_url =image_url, report_url=pdf_url)

#Given a format Report_MD_{timestamp}.pdf, get the timestamp
def getTimeStamp(object_url):
    # Remove the ".pdf" extension
    filename_without_extension = object_url[:-4]

    # Split the remaining string by dot (".")
    split_result = filename_without_extension.split(".")

    # Take the last two elements
    if len(split_result) >= 2:
        last_two_elements = split_result[-2:]

        # Join the last two elements with a dot (".")
        result = ".".join(last_two_elements)
        print(result)
        return result
    else:
        print("Filename format not as expected.")
        return None


def getTimeAndDate(timestamp):
    return datetime.fromtimestamp(float(timestamp)).strftime("%d/%m/%Y %H:%M:%S")

@student_controller.route('/progress', methods=['GET'])
@require_session
def progress():
    student_id = session['student_id']
    print("student id: ", student_id)
    image_url = "https://{0}.s3.amazonaws.com/students/{1}/profile.png".format(custombucket,student_id)
    reports = getProgressionReports(student_id)

    return render_template('student/progress.html', reports=reports,data=[],image_url=image_url)


@student_controller.route('/uploadProgress', methods=['POST'])
@require_session
def uploadProgressReport():
    file = request.files['file']
    #check file type is pdf
    if file.filename.split('.')[1] != 'pdf':
        status = "Error: File is not pdf"
        print(status)
        return status
    
    #Get the student id, and today's date, to generate the file
    student_id = session['student_id']
    now = datetime.now()
    ts = now.timestamp()

    path = f'students/{student_id}/progression_report_{ts}.pdf'

    uploadToS3(file, path) 
    return "Success"

@student_controller.route('/companies', methods=['GET'])
@require_session
def companies():
    student_id = session['student_id']
    image_url = "https://{0}.s3.amazonaws.com/students/{1}/profile.png".format(custombucket,student_id)
    return render_template('student/companies.html', image_url=image_url, data=[])

@student_controller.route('/apply', methods=['POST'])
@require_session
def apply_internship():
    connection = get_database_connection()
    job_offer_id = request.form['id']
    print("job_offer_id: ", job_offer_id)
    return 'Success'
