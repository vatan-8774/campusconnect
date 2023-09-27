from django.urls import path
from . import views

urlpatterns = [

    # URL for the signup view
    path("", views.signup, name="signup"),

    # URL for the index view (requires login)
    path("index/", views.index, name="index"),

    # URL for the login view
    path("login/", views.login_view, name="login"),

    # URL for the logout view
    path("logout_view/", views.logout_view, name="logout_view"),

    # URL for My Profile
    path("my_profile/", views.my_profile, name="my_profile"),

    # URL for Discover
    path("discover/", views.discover, name="discover"),

    # URL for Settings
    path("settings/", views.settings, name="settings"),
    
]
