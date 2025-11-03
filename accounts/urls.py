from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("update/", views.update_profile_and_user, name="update"),
    path("logout/", views.custom_logout, name="custom_logout"),
    path("change_password/", views.change_password, name="change_password"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login")
]
