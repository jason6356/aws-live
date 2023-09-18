#import database 
from services.database_service import get_database_connection

def get_all_lecturers():
    connection = get_database_connection()

    query = "SELECT * FROM Lecturer"
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
    
def get_lecturer_by_id(lecturer_id):
    connection = get_database_connection()

    query = "SELECT * FROM Lecturer WHERE lecturer_id = %s"
    cursor = connection.cursor()

    try:
        cursor.execute(query, lecturer_id)
        return cursor.fetchone()
    except Exception as e:
        print(str(e))
        return False
    finally:
        cursor.close()
        connection.close()
