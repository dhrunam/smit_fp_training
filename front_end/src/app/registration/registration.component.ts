import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { FormGroup , FormControl , Validators, FormBuilder } from '@angular/forms'; 
import { Router } from '@angular/router';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  errorMessage: string |null=null;
  registartionform= new FormGroup({
    username: new FormControl('', Validators.required),
    first_name: new FormControl('', Validators.required),
    last_name:new FormControl ('', Validators.required),
    email: new FormControl('', (Validators.required, Validators.email)),
    password: new FormControl('', (Validators.required, Validators.minLength(8))),
    group: new FormControl('',Validators.required),
    addressline1: new FormControl('', Validators.required),
    addressline2:new FormControl (''),
    post_office: new FormControl('', Validators.required),
    city: new FormControl('', Validators.required),
    district: new FormControl('', Validators.required),
    state: new FormControl('', Validators.required),
    pin: new FormControl('' , Validators.required),
  })
  constructor(private fb:FormBuilder , private http:HttpClient , private router:Router){}
  onSubmit(){
    const formData = this.registartionform.value;
    this.http.post('http://127.0.0.1:8000/api/account/registeruser', formData)
      .subscribe({
        next: (response) => {
          // Registration successful, handle response (e.g., redirect to login)
          console.log('Registration successful:', response);
          
          this.router.navigate(['/login']) ;
        },
        error: (error) => {
          // Handle registration errors gracefully
          this.errorMessage = error.message || 'Registration failed. Please try again later.';
          console.error('Registration error:', error);
          this.registartionform.reset();
        },
      });
  }
}
