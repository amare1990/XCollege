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
        fields = ['user', 'bio', 'role', 'department', 'title', 'position']

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
        fields = ['name', 'academic_year', 'semester','department']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            # 'teachers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # 'students': forms.SelectMultiple(attrs={'class': 'form-control'}),
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
        self.fields['course'].queryset = Course.objects.filter(department=head_department)
        self.fields['teachers'].queryset = UserProfile.objects.filter(department=head_department, role='teacher')

class OfferPositionForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    teachers = forms.ModelChoiceField(queryset=UserProfile.objects.filter(role='teacher'), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))


# class CourseSelectionForm(forms.Form):
#     course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

# class AssessmentForm(forms.ModelForm):
#     class Meta:
#         model = Assessment
#         fields = ['assessment_name', 'student', 'marks']

# AssessmentFormSet = formset_factory(AssessmentForm, extra=0)

class AddMarksForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    assessments = forms.ModelMultipleChoiceField(queryset=Assessment.objects.all(), widget=forms.CheckboxSelectMultiple)
    def __init__(self, teacher_id, *args, **kwargs):
           super(AddMarksForm, self).__init__(*args, **kwargs)
           self.fields['course'].queryset = Course.objects.filter(teachers=teacher_id)
