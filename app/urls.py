from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.IndexView.as_view(), name=f"{app_name}-index"),
    path("home/", views.HomeView.as_view(), name=f"{app_name}-home"),
]