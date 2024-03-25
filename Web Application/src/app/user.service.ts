import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  userBehaviourSubject=new BehaviorSubject(null)
  userTypeBehaviourSubject = new BehaviorSubject(null)
 
  loginStatus:boolean= false;
  constructor(public httpClientObj: HttpClient) {

  }
  addUserToDatabase(userObj: any) {
    console.log(userObj);
    return this.httpClientObj.post("http://127.0.0.1:5000/patient_signup", userObj);
  }

  loginUser(userObj: any): Observable<any> {
   
    return this.httpClientObj.post("http://127.0.0.1:5000/user_login", userObj);

  }

  getUsername(){
    return this.userBehaviourSubject;
  }
  getUserType(){
    return this.userTypeBehaviourSubject;
  }
  userLogout(){
    localStorage.removeItem("token")
   
    this.userBehaviourSubject.next(null)
  }
}
