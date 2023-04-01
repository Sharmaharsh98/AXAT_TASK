from django.urls import path
from .views import admin_panel

urlpatterns = [
    path('admin1', admin_panel, name='admin1')
]