from django.db import models
from django.contrib.auth.models import User

title_choices = (
  ('Mr.', 'Mr.'),
  ('Mrs.', 'Mrs.'),
  ('Dr.', 'Dr.'),
  ('Professor', 'Professor'),
  ('Assistant Professor', 'Assistant Professor'),
  ('Associate Professor', 'Associate Professor')
)

year = (
  ('1st', 'First'),
  ('2nd', 'Second'),
  ('3rd', 'Third'),
  ('4th', 'Fourth'),
  ('5th', 'Fifth')
)

semester= (
  ('1st', 'First'),
  ('2nd', 'Second'),
  ('summer', 'Summer')
)

roles = (
  ('admin', 'admin'),
  ('head', 'head'),
  ('teacher', 'teacher'),
  ('staff', 'staff'),
  ('student', 'student')
)


class Department(models.Model):
  name = models.CharField(max_length=50)
  department_head = models.CharField(max_length=50)

  def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Enter your bio briefly')
    role = models.CharField(max_length=20, choices=roles, default='student')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    academic_year = models.CharField(max_length=20, choices=year, null=True, blank=True)
    semester = models.CharField(max_length=20, choices=semester, null=True, blank=True)
    title = models.CharField(max_length=20, choices=title_choices, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(UserProfile, related_name="courses_taught", null=True, blank=True)
    students = models.ManyToManyField(UserProfile, related_name="courses_registered", null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
