from django.db import models
from website.models import Profile

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

class Teacher(Profile):
  title = models.CharField(max_length=20, choices=title_choices)

class Student(Profile):
  academic_year = models.CharField(max_length=20, choices=year)
  semester = models.CharField(max_length=20, choices=semester)

class Course(models.Model):
   name = models.CharField(max_length=100)
   teacher = models.ManyToManyField(Teacher)
   students = models.ManyToManyField(Student)
