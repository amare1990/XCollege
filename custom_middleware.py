# custom_middleware.py
from django.shortcuts import redirect

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = request.user.profile  # Assuming you have a one-to-one relationship between User and Profile
            if profile.role is None or profile.position is None:
                return redirect('home')

        response = self.get_response(request)
        return response
