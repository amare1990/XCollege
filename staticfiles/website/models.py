from django.db import models
from django.contrib.auth.models import User

roles = (
  ('admin', 'admin'),
  ('head', 'head'),
  ('teacher', 'teacher'),
  ('staff', 'staff'),
  ('student', 'student')
)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  role = models.CharField(max_length=20, choices=roles, default='student')
  profile_picture = models.ImageField(upload_to='profile_pictures/', default='default_profile.jpeg')

  def __str__(self):
    return str(self.user)
