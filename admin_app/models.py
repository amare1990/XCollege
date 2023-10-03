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

class Teacher(Profile):

  title = models.CharField(max_length=20, choices=title_choices)
