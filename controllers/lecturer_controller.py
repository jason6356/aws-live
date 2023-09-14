from flask import Blueprint, request, render_template, url_for, redirect

lecturer_controller = Blueprint('lecturer_controller', __name__)

@lecturer_controller.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('lecturer/dashboard.html', data=[])