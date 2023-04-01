from django.contrib import admin

from .models import TeacherImageModel, StudentImageModel


@admin.register(TeacherImageModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']


@admin.register(StudentImageModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'created_by']