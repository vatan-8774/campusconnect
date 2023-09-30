# social_network/views.py
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.shortcuts import redirect
from django.middleware import csrf
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime
import logging
from django.db.models import F
from django.contrib import messages
from .models import User
from datetime import datetime
from django.http import HttpResponseServerError

@login_required
def index(request):
    show_signup_content = not request.user.is_authenticated

    if request.method == "POST":
        # Handle user signup
        # ...

        # Log the user in after signup
        login(request, user)
        show_signup_content = False  # After signup, don't show signup content

    return render(request, 'social_network/index.html', {'show_signup_content': show_signup_content})



@login_required
def my_profile(request):
    if request.method == "POST":
        print(request.POST)
        # Get the current user
        user = request.user
        

        # Update the user fields based on form input, but only if a value is provided
        if request.POST.get("first-name") is not None:
            user.first_name = request.POST.get("first-name")
        if request.POST.get("last-name") is not None:
            user.last_name = request.POST.get("last-name")
        if request.POST.get("gender") is not None:
            user.gender = request.POST.get("gender")
        if request.POST.get("department") is not None:
            user.department = request.POST.get("department")
        if request.POST.get("year-of-study") is not None:
            user.year_of_study = request.POST.get("year-of-study")
        
        
        

        # Save the user object
        user.save()
        return render(request, 'social_network/my_profile.html')
    return render(request, 'social_network/my_profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_id = request.POST.get('user-id')
        new_first_name = request.POST.get('first-name')
        new_last_name = request.POST.get('last-name')
        new_gender = request.POST.get('gender')
        new_department = request.POST.get('department')
        new_year_of_study = request.POST.get('year-of-study')

        try:
            user = User.objects.get(id=user_id)

            # Update fields if new values are provided
            if new_first_name is not None:
                user.first_name = new_first_name
            if new_last_name is not None:
                user.last_name = new_last_name
            if new_gender is not None:
                user.gender = new_gender
            if new_department is not None:
                user.department = new_department
            if new_year_of_study is not None:
                user.year_of_study = new_year_of_study

            # Handle profile photo upload
            if 'profile-photo' in request.FILES:
                profile_photo = request.FILES['profile-photo']
                user.profile_photo = profile_photo  # Assuming you have a profile_photo field in your User model

            # Save the updated user object
            user.save()

            messages.success(request, "Profile updated successfully.")
            return redirect("my_profile")

        except User.DoesNotExist:
            messages.error(request, "An error occurred while updating the profile.")

    # Handle other cases or return an error response if needed
    return HttpResponseServerError("Invalid request.")  # You can customize this error message


@login_required
def update_bio(request):
    if request.method == 'POST':
        user_id = request.user.id
        new_bio = request.POST.get('bio')

        try:
            user = User.objects.get(id=user_id)

            # Update the bio field if a new value is provided
            if new_bio is not None:
                user.bio = new_bio

            # Save the updated user object
            user.save()

            messages.success(request, "Bio updated successfully.")
            return redirect("my_profile")

        except User.DoesNotExist:
            messages.error(request, "An error occurred while updating the bio.")

    # Handle other cases or return an error response if needed
    return HttpResponseServerError("Invalid request.")  # You can customize this error message



def discover(request):
    return render(request, 'social_network/discover.html')

def settings(request):
    return render(request, 'social_network/settings.html')


def login_view(request):

    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "social_network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:

        return render(request, "social_network/login.html", {'csrf_token': csrf.get_token(request)})


def logout_view(request):
    logout(request)
    return render(request, "social_network/login.html", {'csrf_token': csrf.get_token(request)})



@csrf_exempt  # You may need to exempt CSRF protection for this view
def signup(request):
    if request.method == "POST":
        # Takes in the user username and email submitted in the signup form
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "social_network/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create a new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "social_network/signup.html", {
                "message": "Username already taken."
            })
        
        # Log the user in
        login(request, user)

        # Render the index page with the specified content
        return render(request, 'social_network/index.html', {
            "show_content": True  # Add this context variable
        })
    else:
        return render(request, "social_network/signup.html", {'csrf_token': csrf.get_token(request)})
