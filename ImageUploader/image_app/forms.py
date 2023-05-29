from django import forms
from .models import TeacherImageModel


class TeacherImageForm(forms.ModelForm):

    class Meta:
        model = TeacherImageModel
        fields = ('title', 'image', 'created_by')

# class StudentImageForm(forms.Form):
#         title = forms.CharField()
#         image = forms.ImageField()
#         created_by = forms.CharField()
