import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { BookmarkedComponent } from './bookmarked/bookmarked.component';
import { LoginComponent } from './login/login.component';


const routes: Routes = 
[
  // Fix the routing below vvvvv
  { path: 'home', component: HomeComponent},
  { path: 'bookmarked', component: BookmarkedComponent},
  { path: 'login', component: LoginComponent},
  { path: 'home', component: HomeComponent},
  { path: '', redirectTo: 'home', pathMatch: 'full' },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule
{ 




}
