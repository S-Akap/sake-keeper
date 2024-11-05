from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("home/", views.HomeView.as_view(), name="home"),

    path("restaurants/", views.RestaurantView.as_view(), name="restaurant-index"),
    path("restaurants/list", views.RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurants/create", views.RestaurantCreateView.as_view(), name="restaurant-create"),
    path("restaurants/<int:pk>", views.RestaurantDetailView.as_view(), name="restaurant-detail"),
    path("restaurants/<int:pk>/edit", views.RestaurantEditView.as_view(), name="restaurant-edit"),

    path("bottle-managements/", views.BottleManagementView.as_view(), name="bottle-management-index"),
    path("bottle-managements/list", views.BottleManagementListView.as_view(), name="bottle-management-list"),
    path("bottle-managements/create", views.BottleManagementCreateView.as_view(), name="bottle-management-create"),
    path("bottle-managements/<int:pk>", views.BottleManagementDetailView.as_view(), name="bottle-management-detail"),
    path("bottle-managements/<int:pk>/edit", views.BottleManagementEditView.as_view(), name="bottle-management-edit"),
    path("bottle-managements/<int:pk>/delete", views.BottleManagementDeleteView.as_view(), name="bottle-management-delete"),

    path("bottles/", views.BottleView.as_view(), name="bottle-index"),
    path("bottles/list", views.BottleListView.as_view(), name="bottle-list"),
    path("bottles/create", views.BottleCreateView.as_view(), name="bottle-create"),
    path("bottles/<int:pk>", views.BottleDetailView.as_view(), name="bottle-detail"),
    path("bottles/<int:pk>/edit", views.BottleEditView.as_view(), name="bottle-edit"),
    path("bottles/<int:pk>/delete", views.BottleDeleteView.as_view(), name="bottle-delete"),
    path('bottle/<int:pk>/change-is-empty', views.BottleToggleIsEmptyView.as_view(), name='bottle-change-is-empty'),
]