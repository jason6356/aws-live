from services.database_service import *
from services.s3_service import *
from datetime import date, datetime, time

def create_student(data):
    connection = get_database_connection()
    student_id = data.form['student_id']
    student_name = data.form['student_name']
    student_nric = data.form['student_nric']
    student_gender = data.form['student_gender']
    student_programme = data.form['student_programme']
    student_email = data.form['student_email']
    student_mobile = data.form['mobile_number']
    resume_file = data.files['resume']
    image_file = data.files['student_image']
    lecturer_id = "p123"
    
    insert_sql = "INSERT INTO Student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = connection.cursor()
    image_path = f"students/{student_id}/profile.png"
    resume_path = f"students/{student_id}/resume.pdf"
    uploadToS3(image_file, image_path)
    uploadToS3(resume_file, resume_path)
    image_url = get_object_url(image_path)
    resume_url = get_object_url(resume_path)
    try:
        cursor.execute(insert_sql, (student_id, student_name, student_nric, student_gender, student_programme,student_email, student_mobile,image_url,resume_url,lecturer_id))
        connection.commit()
        print("Successfully Uploading into Database")
        uploadToS3(resume_file, f'students/{student_id}/resume.pdf')
        cursor.close()
        return True

    except Exception as e:
        cursor.close()
        print(str(e))
        return False

    finally:
        connection.close()

def get_student(student_id):
    connection = get_database_connection()
    get_sql = 'SELECT * FROM Student WHERE student_id = %s'
    cursor = connection.cursor()
    try:
        cursor.execute(get_sql, student_id)
        return cursor.fetchone()
    except Exception as e:
        print(str(e))
        return False
    finally:
        cursor.close()
        connection.close()
    
def get_all_students():
    connection = get_database_connection()

    query = "SELECT * FROM Student"
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(str(e))
        return False
    finally:
        cursor.close()
        connection.close()

#write a function to remove student
def remove_student(student_id):
    connection = get_database_connection()

    delete_query = "DELETE FROM Student WHERE student_id = %s"
    cursor = connection.cursor()

    try:
        cursor.execute(delete_query, student_id)
        return True
    except Exception as e:
        print(str(e))
        return False
    finally:
        cursor.close()
        connection.close()

#Write a function to create job application based on student_id and offer_id
def apply_company(student_id, offer_id):
    connections = get_database_connection()
    #Get date now
    dateNow = datetime.now()
    status = "pending"

    insert_query = "INSERT INTO InternshipApplication VALUES(%s, %s, %s, %s)"

    cursor = connections.cursor()
    try:
        cursor.execute(insert_query, (student_id, offer_id, dateNow.strftime("%Y-%m-%d %H:%M:%S"), status))
        connections.commit()
        return True
    except Exception as e:
        print(str(e))
        return False
    finally:
        cursor.close()
        connections.close()
    
def get_detail_applied_internships(student_id):
    connection = get_database_connection()
    query = "SELECT IO.job_title, IO.job_description, IO.allowance, C.company_name, IA.application_date FROM InternshipOffer IO INNER JOIN Company C ON IO.company_id = C.company_id INNER JOIN InternshipApplication IA ON IO.offer_id = IA.offer_id WHERE IA.student_id = %s"
    cursor = connection.cursor()
    try:
        cursor.execute(query, student_id)
        return cursor.fetchall()
    except Exception as e:
        print(str(e))
        return False
    finally:
        cursor.close()
        connection.close()


def get_applied_internships(student_id):
    connection = get_database_connection()
    query = "SELECT offer_id FROM InternshipApplication WHERE student_id = %s"

    cursor = connection.cursor()
    try:
        cursor.execute(query, student_id)
        return cursor.fetchall()
    except Exception as e:
        print(str(e))
        return False
    finally:
        cursor.close()
        connection.close()
