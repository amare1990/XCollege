from django.db import models
from django.contrib.auth.models import User

title_choices = (
  ('Mr.', 'Mr.'),
  ('Mrs.', 'Mrs.'),
  ('Dr.', 'Dr.'),
  ('Assistant Professor', 'Assistant Professor'),
  ('Associate Professor', 'Associate Professor'),
  ('Professor', 'Professor'),
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
    ('summer', 'Summer'),
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
    name = models.CharField(max_length=50)
    school_dean = models.ForeignKey(
        'UserProfile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='school_dean',
    )

    def __str__(self):
        return self.name if self.name else "Unnamed School"


class Department(models.Model):
    name = models.CharField(max_length=50)
    # department_head = models.OneToOneField('UserProfile', on_delete=models.SET_NULL, related_name='department_head', blank=True, null=True)
    department_head = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            admin= UserProfile.objects.get(user__is_superuser=True)
            self.department_head = admin
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else "Unnamed Department"

class Stream(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    chair = models.CharField(max_length=50)

    def __str__(self):
        return self.name if self.name else "Unnamed Stream"

class Program(models.Model):
    program_name = models.CharField(max_length=50, choices=program_name)
    program_type = models.CharField(max_length=50, choices=program_type)
    stream = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
        ('student', 'Student')
    )
    TITLE_CHOICES = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Dr.', 'Dr.'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Professor', 'Professor'),
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

    POSITION = (
        ('head', 'Head'),
        ('school dean', 'School Dean'),
        ('chair', 'Chair'),
        ('program coordinator', 'Program Coordinator'),
        ('college dean', 'College Dean')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Enter your bio briefly')
    role = models.CharField(max_length=20, choices=roles)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    academic_year = models.CharField(max_length=20, choices=year, null=True, blank=True)
    semester = models.CharField(max_length=20, choices=semester, null=True, blank=True)
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, null=True, blank=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=50, choices=position, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default_profile.jpg')

    updated_by_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    course_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(UserProfile, related_name="courses_taught", blank=True)
    students = models.ManyToManyField(UserProfile, related_name="courses_registered", blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, default=1)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    academic_year = models.CharField(max_length=20, choices=year)
    semester = models.CharField(max_length=20, choices=semester)
    is_offered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=8)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=4)
    assessment_name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.assessment_name} - {self.weight}"

class Mark(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    comment = models.CharField(max_length=100, blank=True, null=True, default='Ok!')

class LeaveRequest(models.Model):
    status = (('pending', 'Pending'),
              ('is_approved', 'Approved'),
              ('is_rejected', 'Rejected'),
              )
    requested_by = models.ForeignKey(UserProfile, related_name='leave_requests_requested_by', on_delete=models.CASCADE)
    requested_to = models.ForeignKey(UserProfile, related_name='leave_requests_requested_to', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=status, default='pending')
    # is_approved = models.BooleanField(default=False)
    # is_rejected = models.BooleanField(default=False)
    leave_request_comments = models.TextField(blank=True)
    notification_viewed = models.BooleanField(default=False)

class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class ClassSchedule(models.Model):
    day = models.CharField(max_length=20)
    time = models.TimeField()
    class_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name} - {self.day} - {self.time}"

