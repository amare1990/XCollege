from django.contrib import admin
from .models import UserProfile, Course, Assessment, Department

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Assessment)
admin.site.register(Department)
