from django import forms
from .models import StudentImageModel, TeacherImageModel


class TeacherImageForm(forms.ModelForm):

    class Meta:
        model = TeacherImageModel
        fields = ('title', 'image', 'created_by')

class StudentImageForm(forms.ModelForm):

    class Meta:
        model = StudentImageModel
        fields = ('title', 'image','created_by')
    