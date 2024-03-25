from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
from app import models
from pymongo import MongoClient
app = Flask(__name__)
bcrypt = Bcrypt()

# Connect to MongoDB
client = MongoClient('mongodb+srv://MediCare:gADQCGcPBlY9cuU9@medicare.qqhepv5.mongodb.net/')
db = client['MediCare']
doctor_collection = db['Doctor']
user_collection = db['Patient']

def create_user(new_user):


    user_obj_from_db = user_collection.find_one({"username": new_user["username"]})

    if user_obj_from_db is not None:
        return jsonify({"message": "Username already exists"}), 400

    # hashed_password = bcrypt.generate_password_hash(new_user["password"]).decode("utf-8")
    # new_user["password"] = new_user["password"]
    new_user_id = user_collection.insert_one(new_user).inserted_id

    # Convert ObjectId to string
    new_user["_id"] = str(new_user_id)

    # new_user_obj = user_collection.insert_one(new_user)
    # new_user_obj.save()

    return jsonify({"message": "User created", "payload": new_user}), 200


def user_login(login_user):
    # Retrieve login credentials from the request
    username = login_user.get("username")
    password = login_user.get("password")

    # Find the doctor document by username
    user_waiting_to_login = user_collection.find_one({"username": username})

    # Check if the doctor is not found
    if user_waiting_to_login is None:
        return jsonify({"message": "User not found"}), 404

    # Check if the password is invalid
    if user_waiting_to_login["password"] != password:
        return jsonify({"message": "Invalid password"}), 401
    user_waiting_to_login["_id"] = str(user_waiting_to_login["_id"])

    # If the credentials are valid, return success message
    return jsonify({"message": "login success", "user": user_waiting_to_login}), 200

def get_doctors():
    # doctors = doctor_collection.find
    doctors = list(doctor_collection.find())
    # doctors["_id"] = str(doctors["_id"])
    for doctor in doctors:
        doctor['_id'] = str(doctor['_id'])
    return jsonify({"message": "Doctors data", "payload": doctors}), 200

def get_doctor_by_username(username):
    doctor_from_db = doctor_collection.find_one({"username": username})
    # doctor_from_db = models.doctor_schema.objects(username=username).first()

    if doctor_from_db is None:
        return jsonify({"message": "Doctor not found"}), 404

    return jsonify({"message": "Doctor found", "payload": doctor_from_db}), 200

def not_found(error):
    return jsonify({"message": f"Path {request.path} is not found"}), 404

def handle_error(error):
    return jsonify({"message": "Error!", "payload": str(error)}), 500
