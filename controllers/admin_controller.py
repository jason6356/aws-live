from flask import Blueprint, request, render_template, url_for, redirect, session
from models import admin_model, student_model, lecturer_model, company_model


admin_controller = Blueprint('admin_controller', __name__)

#render admin login
@admin_controller.route('/login', methods=['GET'])
def render_login():
    return render_template('admin/adminLogin.html')

@admin_controller.route('/login', methods=['POST'])
def login():

    adminData = admin_model.get_admin()
    lecturerData = lecturer_model.get_all_lecturers()
    studentData =  student_model.get_all_students()
    companyData = company_model.get_all_companies()

    print("User Loggin In")

    if isAdminAccount(request, adminData):
        session['userType'] = 'admin'
        return redirect('/admin/dashboard')
    
    if isLecturerAccount(request, lecturerData):
        session['userType'] = 'lecturer'
        return redirect('/lecturer/dashboard')

    if isStudentAccount(request, studentData):
        session['userType'] = 'student'
        return redirect('/student/dashboard')
    
    if isCompanyAccount(request, companyData):
        session['userType'] = 'company'
        return redirect('/company/dashboard')

    return render_template('error.html', error_msg='Invalid Name Or Password')

@admin_controller.route('/logout', methods=['GET'])
def logout():
    session.clear()
    print("User Logged Out")
    return redirect('/')

def isCompanyAccount(request, data):
    for row in data:
        print(f"Company row : {row}")
        if request.form['email'] == row[5] and request.form['password'] == row[6]:
            session['company_id'] = row[0]
            return True
        else:
            return False

    return False

def isLecturerAccount(request, data):
    for row in data:
        print(f"Lecturer row : {row}")
        if request.form['email'] == row[2] and request.form['password'] == row[3]:
            return True
        else:
            return False

def isAdminAccount(request, data):
    if request.form['email'] == data[1] and request.form['password'] == data[2]:
        return True
    else:
        return False

def isStudentAccount(request, data):
    for row in data:
        print(f"Student row : {row}")
        if request.form['email'] == row[5] and request.form['password'] == row[2]:
            session['student_id'] = row[0]
            return True

    return False

def isCompanyAccount(request, data):
    for row in data:
        print(f"Company row : {row}")
        if request.form['email'] == row[5] and request.form['password'] == row[6]:
            session['company_id'] = row[0]
            return True

    return False

@admin_controller.route('/dashboard', methods=['GET'])
def dashboard():
    #Fetch requesting companies
    companies = company_model.get_companies_by_status('requested')
    return render_template('admin/dashboard.html', companies=companies)

    
@admin_controller.route('/companies', methods=['GET'])
def companies():
    return render_template('admin/companies.html', data=[])


@admin_controller.route('/lecturers', methods=['GET'])
def lecturers():
    return render_template('admin/lecturers.html', data=[])

@admin_controller.route('/student', methods=['GET'])
def students():
    return render_template('admin/students.html', data=[])


@admin_controller.route('/approveCompany', methods=['POST'])
def approveCompany():
    company_id = request.form['company_id']
    print(company_id)
    company_model.update_company_status(company_id)
    return "Success"







    
