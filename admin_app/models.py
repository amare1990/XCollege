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
  # ('head', 'head'),
  ('teacher', 'teacher'),
  ('staff', 'staff'),
  ('student', 'student')
)

program_type = (
    ('summer', 'summer'),
    ('Extension', 'Extension'),
    ('Regular', 'Regular')
)

program_name = (
    ('PhD', 'PhD'),
    ('MSc.', 'MSc.'),
    ('BSc.', 'BSc.')
)

position = (
    ('head', 'Head'),
    ('school dean', 'School Dean'),
    ('chair', 'Chair'),
    ('program coordinator', 'Program Coordinator'),
    ('college dean', 'College Dean')
)

class School(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    school_dean = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Stream"


class Department(models.Model):
  name = models.CharField(max_length=50, null=True, blank=True)
  department_head = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
        return self.name if self.name else "Unnamed Stream"

class Stream(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    chair = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Stream"

class Program(models.Model):
    name = models.CharField(max_length=50, choices=program_name)
    program_type = models.CharField(max_length=50, choices=program_type)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

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
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=50, choices=position, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(UserProfile, related_name="courses_taught", blank=True)
    students = models.ManyToManyField(UserProfile, related_name="courses_registered", blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    academic_year = models.CharField(max_length=20, choices=year, default='first')
    semester = models.CharField(max_length=20, choices=semester, default='first')


    def __str__(self):
        return self.name
