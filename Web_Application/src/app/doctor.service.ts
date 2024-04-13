import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
// import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DoctorService {
  loginStatus:boolean= false;
  constructor(private httpClientObj: HttpClient) { }
  checkDoctorAvailability(doctor_id: string, slot: string, date : string): Observable<any> {
    return this.httpClientObj.post<any>('http://ec2-3-144-21-20.us-east-2.compute.amazonaws.com/check_doctor_availability', { doctor_id, slot, date });
  }

  // Function to book appointment
  bookAppointment(appointmentDetails: any): Observable<any> {
    return this.httpClientObj.post<any>('http://ec2-3-144-21-20.us-east-2.compute.amazonaws.com/book_appointment', appointmentDetails);
  }
  loginDoctor(userObj: any): Observable<any> {
    return this.httpClientObj.post('http://ec2-3-144-21-20.us-east-2.compute.amazonaws.com'+"/doctor_login", userObj);
  }
  addDoctorToDatabase(userObj: any): Observable<any> {
    return this.httpClientObj.post('http://ec2-3-144-21-20.us-east-2.compute.amazonaws.com'+"/doctor_signup", userObj);
  }

  //get doctor values based on book appointment button selection
  doctorBehaviourSubject = new BehaviorSubject(null);
  logoutdoctorBehaviourSubject = new BehaviorSubject(null);
  getDoctorData() {
    return this.doctorBehaviourSubject
  }
  //get appointment details after successfull payment
  appointmentBehaviourSubject = new BehaviorSubject(null);
  getAppointmentDetails() {
    return this.appointmentBehaviourSubject
  }
  //getAccountPageDetails
  accountBehaviourSubject = new BehaviorSubject(null);
  getAccountPageDetails() {
    return this.accountBehaviourSubject
  }
  // getDoctorList
  getDoctorList(): Observable<any> {
    return this.httpClientObj.get<any>('http://ec2-3-144-21-20.us-east-2.compute.amazonaws.com/get_doctors')
  }
  getDoctorName(){
    return this.logoutdoctorBehaviourSubject;
  }
  doctorLogout(){
    localStorage.removeItem("token")
    
    this.logoutdoctorBehaviourSubject.next(null)
  }

}
