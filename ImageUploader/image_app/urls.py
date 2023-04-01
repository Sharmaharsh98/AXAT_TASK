from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.Teach_image_upload_view, name='T_upload'),
    path('upload1/', views.Stu_image_upload_view, name='S_upload'),
    path('home/', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('show1/', views.show1, name='show1'),
]