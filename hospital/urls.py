
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('doctor/', views.doctor, name="doctor"),
    path('blog/', views.blog, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('index/', views.index, name="dasboard"),
    path('contact/', views.contact, name="contact"),
    path('admin_login/', views.Login, name="login"),
    path('logout', views.Logout_admin, name="logout"), 
    path('view_doctor', views.View_Doctor, name="view_doctor"),
    path('view_patient', views.View_Patient, name="view_patient"), 
    path('add_doctor', views.Add_Doctor, name="add_doctor"),
    path('add_patient', views.Add_Patient, name="add_patient"),  
    path('add_appointment', views.Add_Appointment, name="add_appointment"),
    path('view_appointment', views.View_Appointment, name="view_appointment"),
    path('add_patient', views.Add_Patient, name="add_patient"),  
    path('delete_patient<int:pk>/', views.Delete_Patient, name="delete_patient"),
    path('delete_doctor<int:pk>/', views.Delete_Doctor, name="delete_doctor"),
    path('delete_appointment<int:pk>/', views.Delete_Appointment, name="delete_appointment"), 
    
]