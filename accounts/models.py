# from django.db import models
# from django.contrib.auth.models import User

# USER_ROLES = (
#   ('teacher', 'Teacher'),
#   ('student', 'Student'),
#   ('admin', 'Admin'),
#   ('staff', 'Administrative Staff'),
# )

# class InitialUserProfile(models.Model):

#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   role = models.CharField(max_length=50, choices=USER_ROLES)

#   def __str__(self):
#         return self.user.username
