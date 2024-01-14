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
  ('teacher', 'Teacher'),
  ('staff', 'Staff'),
  ('student', 'Student')
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

    ROLE_CHOICES = (
        ('admin', 'admin'),
        # ('head', 'head'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
        ('student', 'Student')
    )
    TITLE_CHOICES = (
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

    SEMESTER= (
        ('1st', 'First'),
        ('2nd', 'Second'),
        ('summer', 'Summer')
    )

    # ACADEMIC_YEAR = (
    #     ('1st', 'First'),
    #     ('2nd', 'Second'),
    #     ('3rd', 'Third'),
    #     ('4th', 'Fourth'),
    #     ('5th', 'Fifth')
    # )

    POSITION = (
        ('head', 'Head'),
        ('school dean', 'School Dean'),
        ('chair', 'Chair'),
        ('program coordinator', 'Program Coordinator'),
        ('college dean', 'College Dean')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Enter your bio briefly')
    role = models.CharField(max_length=20, choices=roles, default='student')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    academic_year = models.CharField(max_length=20, choices=year, null=True, blank=True)
    semester = models.CharField(max_length=20, choices=semester, null=True, blank=True)
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, null=True, blank=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=50, choices=position, null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default_profile.jpg')
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default_profile.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    course_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(UserProfile, related_name="courses_taught", blank=True)
    students = models.ManyToManyField(UserProfile, related_name="courses_registered", blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    academic_year = models.CharField(max_length=20, choices=year, default='first')
    semester = models.CharField(max_length=20, choices=semester, default='first')
    offered = models.BooleanField(default=False)

    # class Meta:
    #     unique_together = ('name', 'department')

    def __str__(self):
        return self.name

class Assessment(models.Model):
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=8)
    assessment_name = models.CharField(max_length=100)
    # comment = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.assessment_name} - {self.weight}"

class Mark(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    comment = models.CharField(max_length=100, blank=True, null=True)

class LeaveRequest(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)
