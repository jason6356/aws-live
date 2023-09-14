from services.database_service import get_database_connection

def add_admin(data):
    connection = get_database_connection()
    admin_id = data.form["admin_id"]
    admin_name = data.form["admin_name"]
    admin_password = data.form["admin_password"]

    insert_sql = "INSERT INTO Admin_User VALUES (%s,%s,%s)"
    cursor = connection.cursor()

    try:
        cursor.execute(insert_sql, (admin_id,admin_name,admin_password))
        connection.commit()
        print("Successfully Uploading Admin into Database")
        cursor.close()
        return True

    except Exception as e:
        cursor.close()
        print(str(e))
        return False

    finally:
        connection.close()

def get_admin():
    connection = get_database_connection()

    query = "SELECT * FROM Admin_User"
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        cursor.close()
        # Return ('admin01', 'admin1', '123456')
        return cursor.fetchone()

    except Exception as e:
        cursor.close()
        print(str(e))
        return False

    finally:
        connection.close()










    



