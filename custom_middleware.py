# custom_middleware.py
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                profile = request.user.userprofile  # Assuming you have a one-to-one relationship between User and Profile
            except User.profile.RelatedObjectDoesNotExist:
                # Handle the case where the User does not have a related Profile
                messages.INFO(request, "Wait unitil your initial profile is created!")
                return redirect('home')  # Replace 'profile_creation' with the actual URL name for profile creation

        response = self.get_response(request)
        return response
