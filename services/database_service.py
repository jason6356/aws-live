from pymysql import connections
from config import *

def get_database_connection():
    connection = connections.Connection(
        host=customhost,
        port=3306,
        user=customuser,
        password=custompass,
        db=customdb
    )
    return connection