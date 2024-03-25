import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { DoctorService } from 'src/app/doctor.service';

@Component({
  selector: 'app-accountpage',
  templateUrl: './accountpage.component.html',
  styleUrls: ['./accountpage.component.css']
})
export class AccountpageComponent implements OnInit {


  accountDetails: any[] = [];
  wallet: number = 100;
  value: number = 0;
  valueFromInput: number;
  payment: boolean = false;

  constructor(public serviceObj:DoctorService, public routerObj: Router, public fb: FormBuilder) { }

  ngOnInit(): void {
    this.accountDetails.push(this.serviceObj.getAccountPageDetails().getValue())
  }

  successfulPayment() {
    if(this.wallet>=this.accountDetails[0].consultationFee){
      this.payment=true
      this.wallet = this.wallet - this.accountDetails[0].consultationFee
      alert("Payment Successful!")
      this.serviceObj.appointmentBehaviourSubject.next(this.accountDetails)
      this.routerObj.navigateByUrl('/userdashboard/appoint')
    }
    
    else{
      this.payment=false
      alert("Insuficient Balance!")
    }
  }

  addToInput(valuefromButton) {
    this.value = this.value + valuefromButton;
  }


  AddMOney = this.fb.group({
    addMoney: ['']
  })


  addToWallet() {
    this.valueFromInput = this.AddMOney.value.addMoney
    console.log(this.AddMOney.value.addMoney);
    this.wallet = this.wallet + this.valueFromInput
  }


}