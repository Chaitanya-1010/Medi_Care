from flask import request, jsonify, Flask, send_file, render_template
# from app_routes import app
# from app.patient_operations import * 
import Backend.patient_operations as patient
import Backend.doctors_operations as doctor
# from app.doctors_operations import * 
from Backend.login import *
from flask_cors import CORS

# Define API endpoints
# app=Flask(__name__)
app = Flask(__name__, static_folder='Backend/static', template_folder="Backend/templates")
# CORS(app) 

@app.route('/')
def index():
    # Implement login logic here
    return render_template("index.html")

# # Login
# @app.route('/user_login', methods=['POST'])
# def userLogin():
#     # Implement login logic here
#     login_user=request.json
#     return patient.user_login(login_user)
#     pass

# @app.route('/doctor_login', methods=['POST'])
# def doctorLogin():
#     login_doctor = request.json
#     return doctor.doctor_login(login_doctor)

# @app.route('/doctor_signup', methods=['POST'])
# def doctor_signup():
#     new_doctor= request.json
#     return doctor.create_doctor(new_doctor)
#     # pass

# @app.route('/patient_signup', methods=['POST'])
# def patient_signup():
#     new_user= request.json
#     return patient.create_user(new_user)

# @app.route('/api/get_doctors', methods=['GET'])
# def getDoctors():
#     return patient.get_doctors()
#     # pass


# # Patient Operations
# @app.route('/api/user_medical-records', methods=['GET'])
# def get_medical_records():
#     # Implement logic to fetch medical records from MongoDB
#     pass

# @app.route('/api/book-appointment', methods=['POST'])
# def book_appointment():
#     # Implement logic to book appointment
#     pass

# # Doctor Operations
# @app.route('/api/doctor_appointments', methods=['GET'])
# def get_appointments():
#     # Implement logic to fetch appointments for the doctor
#     pass

# @app.route('/api/doctor_respond-appointment', methods=['POST'])
# def respond_appointment():
#     # Implement logic for doctor to respond to appointment requests
#     pass


if __name__ == '__main__':
    app.run(host='0.0.0.0')
