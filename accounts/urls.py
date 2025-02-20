""" STANDARD DJANGO IMPORTS """

from django.urls import path

""" LOCAL APP IMPORTS """

from .views import homepage_view, logout_view, signin_view, signup_view, credits_view, welcome_view

urlpatterns = [
    path("", welcome_view, name="welcome"),  # Redirect to the welcome page by default
    path("signup/", signup_view, name="signup"),
    path("signin/", signin_view, name="signin"),
    path("logout/", logout_view, name="logout"),
    path("home/", homepage_view, name="home"),
]