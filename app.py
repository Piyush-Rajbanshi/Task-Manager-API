from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from db_connection import get_connection

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# REGISTER
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully"}), 201


# LOGIN 
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    conn.close()

    if user and user[2] == password:
        access_token = create_access_token(identity=str(user[0]))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# CREATE TASK 
@app.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    title = data["title"]
    description = data.get("description", "")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description, user_id) VALUES (%s, %s, %s)",
        (title, description, user_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Task created"}), 201


# GET TASKS 
@app.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT task_id, title, description FROM tasks WHERE user_id = %s",
        (user_id,)
    )
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)