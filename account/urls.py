from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name="signup"),
    path('log-in/', views.LogInView.as_view(), name="login"),
    path('log-out/', views.LogOutView.as_view(), name="logout"),
    path('sample-login/', views.sample_login, name="sample-login")
]
