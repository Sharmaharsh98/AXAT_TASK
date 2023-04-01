from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup_view, name='signup'),
    path('login/', views.Login_view, name='login'),
    path('logout/', views.Logout_view, name='logout')
]