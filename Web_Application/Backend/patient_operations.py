from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
from Backend import models
from pymongo import MongoClient
import mysql.connector
app = Flask(__name__)
bcrypt = Bcrypt()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['doctor_appointment']
doctor_collection = db['doctorcollection']
user_collection = db['usercollection']

conn = mysql.connector.connect(
    host="database-2.cf6ggqy66qxa.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="sameer123",
    database="medicare"
)


def create_user(new_user):
    # Check if the username already exists in the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE username = %s", (new_user["username"],))
    user = cursor.fetchone()
    if user:
        cursor.close()
        return jsonify({"message": "Username already exists"}), 400

    # Insert the new user record into the patients table
    cursor.execute("INSERT INTO patients (username, password, email, city, phoneno, age, name) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (new_user["username"], new_user["password"], new_user["email"], new_user["city"], new_user["phoneno"], new_user["age"], new_user["name"]))

    conn.commit()

    # Get the inserted user's ID
    new_user_id = cursor.lastrowid

    # Close the cursor
    cursor.close()

    # Return success message and inserted user record
    new_user["_id"] = new_user_id
    return jsonify({"message": "User created", "payload": new_user}), 200


def user_login(login_user):
    # Retrieve login credentials from the request
    username = login_user.get("username")
    password = login_user.get("password")

    # Find the user record by username
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients WHERE username = %s", (username,))
    user = cursor.fetchone()

    # Check if the user is not found
    if user is None:
        cursor.close()
        return jsonify({"message": "User not found"}), 404

    # Check if the password is invalid
    if user["password"] != password:
        cursor.close()
        return jsonify({"message": "Invalid password"}), 401

    # Close the cursor
    cursor.close()

    # If the credentials are valid, return success message and user's information
    return jsonify({"message": "login success", "user": user}), 200

def get_user_by_username(username):
    # Find the doctor record by username
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients WHERE username = %s", (username,))
    doctor = cursor.fetchone()

    # Check if the doctor is not found
    if doctor is None:
        cursor.close()
        return jsonify({"message": "User not found"}), 404

    # Close the cursor
    cursor.close()

    # If the doctor is found, return success message and doctor's information
    return jsonify({"message": "User found", "payload": doctor}), 200

def not_found(error):
    return jsonify({"message": f"Path {request.path} is not found"}), 404

def handle_error(error):
    return jsonify({"message": "Error!", "payload": str(error)}), 500
