from django.shortcuts import render
from image_app.models import TeacherImageModel, StudentImageModel
from django.contrib.auth.decorators import login_required
from auth_app.decorators import admin_only


# Create your views here.
@admin_only
@login_required(login_url='login')
def admin_panel(request):
    data1 = TeacherImageModel.objects.all()
    data = StudentImageModel.objects.all()
    
    template_name = 'admin_app/admin.html'
    context = {'data1': data1, 'data': data}
    return render(request, template_name, context)
