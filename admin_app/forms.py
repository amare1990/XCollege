# forms.py
from django import forms
from django.forms import formset_factory
from .models import UserProfile, Department, Course, Assessment, LeaveRequest

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

# class EditTeacherForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['role', 'department', 'title', 'position', 'bio', 'profile_picture']

#         widgets = {
#             # 'user': forms.Select(attrs={'class': 'form-control'}),
#             'bio': forms.Textarea(attrs={'class': 'form-control'}),
#             'role': forms.Select(attrs={'class': 'form-control'}),
#             'department': forms.Select(attrs={'class': 'form-control'}),
#             'title': forms.Select(attrs={'class': 'form-control'}),
#             'position': forms.Select(attrs={'class': 'form-control'}),
#         }

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
    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        teacher_dept = teacher.department
        super(AssessmentForm, self).__init__(*args, **kwargs)
        if teacher_dept:
            self.fields['course'].queryset = Course.objects.filter(department=teacher_dept)

    class Meta:
        model = Assessment
        fields = ['course', 'assessment_name', 'weight']


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



from django import forms
from admin_app.models import UserProfile

class EditTeacherForm(forms.ModelForm):
    # Fields from the User model
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['role', 'department', 'title', 'position', 'bio', 'profile_picture']

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditTeacherForm, self).__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields.pop('password')  # Remove the 'password' field if it exists

        # Populate initial data from the User model
        if self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        # Save the UserProfile fields
        user_profile = super(EditTeacherForm, self).save(commit=False)
        if commit:
            user_profile.save()

        # Save the User fields
        if user_profile.user:
            user = user_profile.user
            user.username = self.cleaned_data['username']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            if commit:
                user.save()

        return user_profile

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields ='__all__'
        exclude = ('userprofile', 'approved', 'leave_request_comments', 'notification_viewed',)

        widgets = {
        'start_date': forms.DateInput(attrs={'type': 'date'}),
        'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

