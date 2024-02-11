import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { YellowpageComponent } from './yellowpage/yellowpage.component';
import { HttpClientModule } from '@angular/common/http';
import { NavBarComponent } from './yellowpage/nav-bar/nav-bar.component'; 

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegistrationComponent,
    YellowpageComponent,
    NavBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
