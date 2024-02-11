import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { YellowpageComponent } from './yellowpage/yellowpage.component'; 
const routes: Routes = [
  {path:'' , component:RegistrationComponent},
  {path:'login', component:LoginComponent},
  {path:'yellowpage' , component:YellowpageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
