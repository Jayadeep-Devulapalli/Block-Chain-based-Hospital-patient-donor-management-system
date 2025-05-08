from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('HospitalLogin.html', views.HospitalLogin, name="HospitalLogin"), 
	       path('HospitalLoginAction', views.HospitalLoginAction, name="HospitalLoginAction"),
	       path('DonorLogin.html', views.DonorLogin, name="DonorLogin"), 
	       path('DonorLoginAction', views.DonorLoginAction, name="DonorLoginAction"),
	       path('UserLogin.html', views.UserLogin, name="UserLogin"), 
	       path('UserLoginAction', views.UserLoginAction, name="UserLoginAction"),
	       path('Register.html', views.Register, name="Register"),
	       path('Signup', views.Signup, name="Signup"),
	       path('AddPatientHistory.html', views.AddPatientHistory, name="AddPatientHistory"),
	       path('AddPatientHistoryAction', views.AddPatientHistoryAction, name="AddPatientHistoryAction"),
	       path('AddDonorHistory.html', views.AddDonorHistory, name="AddDonorHistory"),
	       path('AddDonorHistoryAction', views.AddDonorHistoryAction, name="AddDonorHistoryAction"),
	       path('MatchOrgans', views.MatchOrgans, name="MatchOrgans"),
	       path('ViewTransplant', views.ViewTransplant, name="ViewTransplant"),
	       path('DonationStatus', views.DonationStatus, name="DonationStatus"),
	       path('ViewRequestStatus', views.ViewRequestStatus, name="ViewRequestStatus"),
	       path('MatchOrganAction', views.MatchOrganAction, name="MatchOrganAction"),
	       path('Alert', views.Alert, name="Alert"),
]