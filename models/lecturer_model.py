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
