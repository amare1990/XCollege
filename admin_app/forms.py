# forms.py
from django import forms
from .models import UserProfile, Department, Course


class AddDepartmentForm(forms.ModelForm):
     department_head = forms.ModelChoiceField(queryset=UserProfile.objects.filter(role='teacher'), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

     class Meta:
        model = Department
        fields = ['name', 'department_head']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'role', 'department', 'academic_year', 'semester']

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
        fields = ['user', 'bio', 'role', 'department', 'title']

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
        }

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'academic_year', 'semester','department']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'academic-year': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            # 'teachers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # 'students': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

class CourseRegistrationForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)
