from flask import Blueprint, render_template, request, redirect, session
from models import company_model

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







