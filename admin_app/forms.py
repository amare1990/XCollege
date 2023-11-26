# forms.py
from django import forms
from .models import UserProfile, Department


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','department_head']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department_head': forms.TextInput(attrs={'class': 'form-control'}),
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
