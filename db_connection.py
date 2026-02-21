import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your_Passsword_Here",
        database="task_manager_db"
    )
