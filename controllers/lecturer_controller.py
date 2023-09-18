from flask import Blueprint, request, render_template, url_for, redirect, session
from models import lecturer_model, student_model
from services.s3_service import getProgressionReports



lecturer_controller = Blueprint('lecturer_controller', __name__)

@lecturer_controller.route('/dashboard', methods=['GET'])
def dashboard():
    students = student_model.get_all_students()
    for student in students:
        print(student)

    return render_template('lecturer/dashboard.html', students=students)

@lecturer_controller.route('/viewProgressReport', methods=['GET'])
def view_progress_report():
    student_id = request.args.get('student_id')
    student = student_model.get_student(student_id)
    reports = getProgressionReports(student_id)
    return render_template('lecturer/viewProgressReport.html', reports=reports, data=[], student=student)

@lecturer_controller.route('/login', methods=['GET'])
def render_login():
    return render_template('lecturer/lecturerLogin.html')

@lecturer_controller.route('/login', methods=['POST'])
def login():
    lecturerData = lecturer_model.get_all_lecturers()
    print("User Loggin In")

    if isLecturerAccount(request, lecturerData):
        session['userType'] = 'lecturer'
        return redirect('/lecturer/dashboard')

def isLecturerAccount(request, data):
    for row in data:
        print(f"Lecturer row : {row}")
        if request.form['email'] == row[2] and request.form['password'] == row[3]:
            return True
        else:
            return False