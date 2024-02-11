import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl , FormGroup , Validators} from '@angular/forms';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  errorMessage: string |null=null;
  loginform = new FormGroup({
    username: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
  })
  constructor(private http:HttpClient , private router:Router){}
  onSubmit(){
    const formData = this.loginform.value;
    this.http.post('http://127.0.0.1:8000/api/account/loginuser', formData)
      .subscribe({
        next: (response) => {
          // Registration successful, handle response (e.g., redirect to login)
          console.log(response);
          this.router.navigate(['/yellowpage'])

        },
        error: (error) => {
          // Handle registration errors gracefully
          this.errorMessage = error.message || 'Registration failed. Please try again later.';
          console.error(error);
          this.loginform.reset();
        },
      });
  }
}
