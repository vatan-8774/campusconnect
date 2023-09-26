from django.urls import path
from . import views

urlpatterns = [

    # URL for the signup view
    path("", views.signup, name="signup"),

    # URL for the index view (requires login)
    path("index/", views.index, name="index"),

    # URL for the login view
    path("login/", views.login_view, name="login"),

    
]
