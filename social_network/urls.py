from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_network.urls')),  # Include your app's URLs here
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [

    # URL for the signup view
    path("", views.signup, name="signup"),

    # URL for the index view (requires login)
    path("index/", views.index, name="index"),

    # URL for the login view
    path("login/", views.login_view, name="login"),

    path("update_bio/", views.update_bio, name="update_bio"),


    # URL for the logout view
    path("logout_view/", views.logout_view, name="logout_view"),

    # URL for My Profile
    path("my_profile/", views.my_profile, name="my_profile"),

    # URL for Discover
    path("discover/", views.discover, name="discover"),

    # URL for Settings
    path("settings/", views.settings, name="settings"),

    path("update_profile/", views.update_profile, name="update_profile"),


    
]
