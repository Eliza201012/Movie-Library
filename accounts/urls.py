from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("update/", views.update_profile_and_user, name="update"),
    path("logout/", views.custom_logout, name="custom_logout"),
    path("change_password/", views.change_password, name="change_password")
]
