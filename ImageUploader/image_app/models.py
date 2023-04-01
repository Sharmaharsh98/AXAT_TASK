from django.db import models
from auth_app.models import User

# Create your models here.
def user_directory_path(instance, filename):
    return 'Teacher_{0}/{1}'.format(instance.created_by.id, filename)

class TeacherImageModel(models.Model):

    title = models.CharField(max_length=100)
    image = models.FileField(upload_to=user_directory_path)
    created_by =  models.ForeignKey(User, on_delete=models.CASCADE)


def user_directory_path(instance, filename):
    return 'Student_{0}/{1}'.format(instance.created_by.id, filename)


class StudentImageModel(models.Model):

    title = models.CharField(max_length=100)
    image = models.FileField(upload_to=user_directory_path)
    created_by =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
