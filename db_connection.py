import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="piyush@1937",
        database="task_manager_db"
    )