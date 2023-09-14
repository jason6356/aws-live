from services.database_service import *

def create_student(data):
    connection = get_database_connection()
    student_id = data.form['student_id']
    student_name = data.form['student_name']
    student_nric = data.form['student_nric']
    student_gender = data.form['student_gender']
    student_programme = data.form['student_programme']
    student_email = data.form['student_email']
    student_mobile = data.form['mobile_number']

    insert_sql = "INSERT INTO Student VALUES(%s, %s, %s, %s, %s, %s, %s)"
    cursor = connection.cursor()

    try:
        cursor.execute(insert_sql, (student_id, student_name, student_nric, student_gender, student_programme,student_email, student_mobile))
        connection.commit()
        print("Successfully Uploading into Database")
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

