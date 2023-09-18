from flask import Blueprint, render_template, request, redirect, session
from models import company_model
from config import *

company_controller = Blueprint('company_controller', __name__)

@company_controller.route('/addCompany', methods=['POST'])
def add_company():
    print("Request Received")
    company_model.add_company(request)
    return redirect('/')

@company_controller.route('/register', methods=['GET'])
def render_register():
    return render_template('/company/addCompany.html')

@company_controller.route('/dashboard', methods=['GET'])
def dashboard():
    company_id = session['company_id']
    company = company_model.get_company_by_id(company_id)
    job_offers = company_model.get_job_offers_from_company_id(company_id)
    return render_template('/company/companyDashboard.html', company=company, job_offers=job_offers)

@company_controller.route('/createJobPost', methods=['POST'])
def createJobPost():
    company_id = session['company_id']
    company_model.create_job_post(request, company_id)
    return "Success"

#write a login function for company
@company_controller.route('/login', methods=['GET'])
def render_login():
    return render_template('company/companyLogin.html')

@company_controller.route('/appliedStudents', methods=['GET'])
def render_applied_student():
    company_id = session['company_id']
    results = company_model.get_student_applications(company_id)
    print(results)
    resume_pdf = "https://{0}.s3.amazonaws.com/{1}.pdf".format(custombucket,results[0][3])
    print(results)
    return render_template('company/appliedStudents.html', applications=results, resume_pdf=resume_pdf)

#Write a function for company login
@company_controller.route('/login', methods=['POST'])
def login():
    companyData = company_model.get_all_companies()
    if isCompanyAccount(request, companyData):
        session['userType'] = 'company'
        return redirect('/company/dashboard')

    return render_template('error.html', error_msg='Invalid Name Or Password')

def isCompanyAccount(request, data):
    for row in data:
        print(f"Company row : {row}")
        if request.form['email'] == row[5] and request.form['password'] == row[6]:
            session['company_id'] = row[0]
            return True

    return False



