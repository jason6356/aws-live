from services.database_service import get_database_connection
from services.s3_service import uploadToS3, get_object_url

#INSERT INTO Company VALUES ("C0001","Sainoforce", "www.google.com", "Wong Jeng Liang", "018-388-7670", "sainoforce@gmail.com", "sainoforce123", "requested");
def add_company(data):
    connection = get_database_connection()
    company_id = data.form['company_id']
    company_name = data.form['company_name']
    company_website = data.form['company_website']
    person_in_charge = data.form['person_in_charge']
    contact_number = data.form['contact_number']
    company_email = data.form['company_email']
    company_password = data.form['company_password']
    company_address = data.form['company_address']
    cert = data.files['cert']
    logo = data.files['logo']
    register_status = 'requested'

    insert_sql = "INSERT INTO Company VALUES (%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s)"
    cursor = connection.cursor()
    certPath = f"companies/{company_id}/cert.pdf"
    logoPath = f"companies/{company_id}/logo.png"
    uploadToS3(cert, certPath)
    uploadToS3(logo, logoPath)
    cert_obj_url = get_object_url(certPath)
    logo_obj_url = get_object_url(logoPath)
    try:
        cursor.execute(insert_sql,(company_id,company_name,company_website,person_in_charge,contact_number,company_email,company_password,register_status,company_address, cert_obj_url, logo_obj_url))
        connection.commit()
        cursor.close()
        print("Successfully Registered a Company")
        return True

    except Exception as e:
        cursor.close()
        print(str(e))
        return None
    
    finally:
        connection.close()

def get_companies_by_status(status='requested'):
    connection = get_database_connection()

    query_sql = "SELECT * FROM Company WHERE register_status = %s"
    cursor = connection.cursor()

    try:
        cursor.execute(query_sql, status)
        print("Fetched")
        return cursor.fetchall()

    except Exception as e:
        cursor.close()
        print(str(e))
        return None
    
    finally:
        connection.close()

def update_company_status(company_id):
    connection = get_database_connection()

    update_sql = "UPDATE Company SET register_status = 'approved' WHERE company_id = %s"
    cursor = connection.cursor()

    try:
        cursor.execute(update_sql,company_id)
        connection.commit()
        print("Successfully Updating the Company Details")
        return True
    
    except Exception as e:
        cursor.close()
        print(str(e))
        return False
    
    finally:
        connection.close()

def get_company_by_id(company_id):
    connection = get_database_connection()

    query_sql = "SELECT * FROM Company WHERE company_id = %s"
    cursor = connection.cursor()

    try:
        cursor.execute(query_sql, company_id)
        print("Successfully Getting the Company Details")
        return cursor.fetchone()

    except Exception as e:
        cursor.close()
        print(str(e))
        return None

    finally:
        connection.close()


def get_all_companies():
    connection = get_database_connection()

    query_sql = "SELECT * FROM Company"
    cursor = connection.cursor()

    try:
        cursor.execute(query_sql)
        print("Successfully Getting the Company Details")
        return cursor.fetchall()

    except Exception as e:
        cursor.close()
        print(str(e))
        return None

    finally:
        connection.close()

def get_job_offers_from_company_id(company_id):
    connection = get_database_connection()

    query_sql = "SELECT * FROM InternshipOffer WHERE company_id = %s"
    cursor = connection.cursor()

    try:
        cursor.execute(query_sql, company_id)
        print("Successfully Getting the Job Offers Details")
        return cursor.fetchall()
    
    except Exception as e:
        cursor.close()
        print(str(e))
        return None
    
    finally:    
        connection.close()

def get_all_job_post():
    connection = get_database_connection()
    query_sql = "SELECT IO.offer_id, IO.job_title, IO.job_description, IO.allowance, IO.company_id, C.company_name, C.company_website, C.person_in_charge, C.contact_number, C.company_email, C.company_address, C.register_status, C.logo_url FROM InternshipOffer IO INNER JOIN Company C ON IO.company_id = C.company_id;"

    cursor = connection.cursor()

    try:
        cursor.execute(query_sql)
        print("Successfully Getting the Job Offers Details")
        return cursor.fetchall()
    except Exception as e:
        cursor.close()
        print(str(e))
        return None

def create_job_post(data, company_id):
    connection = get_database_connection()
    offer_id = data.form['offer_id']
    job_title = data.form['job_title']
    job_description = data.form['job_description']
    allowance = data.form['allowance']

    insert_sql = "INSERT INTO InternshipOffer VALUES (%s,%s,%s,%s,%s)"
    cursor = connection.cursor()

    try:
        cursor.execute(insert_sql,(offer_id,job_title,job_description,allowance,company_id))
        print("Successfully Create the Job Offer")
        connection.commit()
        return True
    
    except Exception as e:
        cursor.close()
        print(str(e))
        return None
    
    finally:    
        connection.close()

def get_all_offer():

    connection = get_database_connection()
    query_sql = "SELECT * FROM InternshipOffer"



def get_student_applications(company_id):
    connection = get_database_connection()
    sql_query = """
    SELECT InternshipOffer.job_title, Student.student_name, InternshipApplication.application_date, Student.student_id, Student.resume_url
    FROM InternshipOffer
    INNER JOIN InternshipApplication ON InternshipOffer.offer_id = InternshipApplication.offer_id
    INNER JOIN Student ON InternshipApplication.student_id = Student.student_id
    WHERE InternshipOffer.company_id = %s;
"""
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, company_id)
        return cursor.fetchall()
        return True
    
    except Exception as e:
        cursor.close()
        print(str(e))
        return None
    
    finally:    
        connection.close()

