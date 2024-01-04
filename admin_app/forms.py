# forms.py
from django import forms
from django.forms import formset_factory
from .models import UserProfile, Department, Course, Assessment

class AddDepartmentForm(forms.ModelForm):
     department_head = forms.ModelChoiceField(queryset=UserProfile.objects.filter(role='teacher'), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

     class Meta:
        model = Department
        fields = ['name', 'department_head']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['user', 'title', 'position', 'bio', 'role', 'department', 'academic_year', 'semester']

#         widgets = {
#             'user': forms.Select(attrs={'class': 'form-control'}),
#             'bio': forms.Textarea(attrs={'class': 'form-control'}),
#             'role': forms.Select(attrs={'class': 'form-control'}),
#             'department': forms.Select(attrs={'class': 'form-control'}),
#             'academic_year': forms.Select(attrs={'class': 'form-control'}),
#             'semester': forms.Select(attrs={'class': 'form-control'}),
#             'position': forms.Select(attrs={'class': 'form-control'}),
#             'title': forms.Select(attrs={'class': 'form-control'}),
#             'semester': forms.Select(attrs={'class': 'form-control'})
#         }


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'role', 'department', 'academic_year', 'semester', 'profile_picture']

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'})
        }

class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'role', 'department', 'title', 'position', 'profile_picture']

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'name', 'academic_year', 'semester','department']

        widgets = {
            'course_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

class CourseRegistrationForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, student_department, *args, **kwargs):
        super(CourseRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['courses'].queryset = Course.objects.filter(department=student_department)

class AddCourseOfferingForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    course = forms.ModelChoiceField(queryset=Course.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}))
    teachers = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.none(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    def __init__(self, head_department, *args, **kwargs):
        super(AddCourseOfferingForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(department=head_department, offered=False)
        self.fields['teachers'].queryset = UserProfile.objects.filter(department=head_department, role='teacher')

class OfferPositionForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    teachers = forms.ModelChoiceField(queryset=UserProfile.objects.filter(role='teacher'), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))


class CourseSelectionForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['assessment_name', 'weight']


class AddMarksForm(forms.Form):
    student = forms.ModelChoiceField(queryset=UserProfile.objects.filter(role='student'))
    assessment = forms.ModelChoiceField(queryset=Assessment.objects.all())
    marks = forms.DecimalField(max_digits=5, decimal_places=2, initial=0)
    comment = forms.CharField(max_length=100)


year = (
  ('1st', 'First'),
  ('2nd', 'Second'),
  ('3rd', 'Third'),
  ('4th', 'Fourth'),
  ('5th', 'Fifth')
)

class AcademicYear(forms.Form):
    year = forms.Select(choices=year)
