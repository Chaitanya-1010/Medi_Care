from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
from Backend import models
# from models import doctor_schema as Doctor  # Import your Doctor model
from pymongo import MongoClient
app = Flask(__name__)
bcrypt = Bcrypt()

# Connect to MongoDB
client = MongoClient('mongodb+srv://MediCare:gADQCGcPBlY9cuU9@medicare.qqhepv5.mongodb.net/')
db = client['MediCare']
doctor_collection = db['Doctor']

def create_doctor(new_doctor):
    # new_doctor = request.json

    # doctor_obj_from_db = models.doctor_schema.objects(username=new_doctor["username"]).first()
    username = new_doctor.get("username")
    # password = new_doctor.get("password")

    # Find the doctor document by username
    doctor_obj_from_db = doctor_collection.find_one({"username": username})


    if doctor_obj_from_db is not None:
        return jsonify({"message": "Username already exists"}), 400

    # hashed_password = bcrypt.generate_password_hash(new_doctor["password"]).decode("utf-8")
    # new_doctor["password"] = hashed_password

    new_doctor_id = doctor_collection.insert_one(new_doctor).inserted_id

    # Convert ObjectId to string
    new_doctor["_id"] = str(new_doctor_id)


    return jsonify({"message": "Doctor created", "payload": new_doctor}), 200


def doctor_login(login_doctor):
    # Retrieve login credentials from the request
    username = login_doctor.get("username")
    password = login_doctor.get("password")

    # Find the doctor document by username
    doctor_waiting_to_login = doctor_collection.find_one({"username": username})

    # Check if the doctor is not found
    if doctor_waiting_to_login is None:
        return jsonify({"message": "Doctor not found"}), 404

    # Check if the password is invalid
    if doctor_waiting_to_login["password"] != password:
        return jsonify({"message": "Invalid password"}), 401
    doctor_waiting_to_login["_id"] = str(doctor_waiting_to_login["_id"])

    # If the credentials are valid, return success message
        # res.status(200).send({ message: "login success", token: signedToken, doctor: doctorWaitingToLogin })
    return jsonify({"message": "login success", "doctor": doctor_waiting_to_login}), 200

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
