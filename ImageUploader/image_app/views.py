
from django.shortcuts import render
from .forms import TeacherImageForm
from .models import StudentImageModel, TeacherImageModel
from auth_app.models import User
from django.contrib.auth.decorators import login_required
from auth_app.views import *

# from auth_app.decorators import allowed_users



# Create your views here.
@login_required(login_url='login')
def Teach_image_upload_view(request):
    form = TeacherImageForm()
    template_name = 'image_app/teacher.html'

    if request.method == 'POST':
        form = TeacherImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, template_name, {'form': form, 'img_obj': img_obj})

    return render(request, template_name, {'form': form})


@login_required(login_url='login')
def Stu_image_upload_view(request):
    print('upload view called')
    # form = StudentImageForm()
    template_name = 'image_app/student.html'

    if request.method == 'POST':
            # print('form is valid')
            title = request.POST['title']
            image = request.FILES['image']
            # print(request.FILES)
            # created_by = request.POST.get('created_by', False)
            # # print(request.POST.get('created_by'))

            f = StudentImageModel(title= title, image = image, created_by = request.user)
            f.save()
            # print('created by user-->>>>',created_by)
            # Get the current instance object to display in the template
            # img_obj = image.instance
            return render(request, template_name, context={})

    return render(request, template_name, {})


@login_required(login_url='login')
def home(request):
    template_name = 'image_app/index.html'
    context = {}

    return render(request, template_name, context)

# Teacher
@login_required(login_url='login')
def show(request):
    data1 = TeacherImageModel.objects.filter(created_by__id=request.user.id)
    data = StudentImageModel.objects.all()
    
    template_name = 'image_app/show.html'
    context = {'data1': data1, 'data': data}
    return render(request, template_name, context)

# student
@login_required(login_url='login')
def show1(request):
    data = StudentImageModel.objects.filter(created_by__id=request.user.id)
    # print(StudentImageModel.objects.filter(created_by__id=request.user.id))
    template_name = 'image_app/show1.html'
    context = {'data': data}
    return render(request, template_name, context)


#  form = StudentImageForm()
#     template_name = 'image_app/student.html'

#     if request.method == 'POST':
#         form = StudentImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, template_name, {'form': form, 'img_obj': img_obj})

#     return render(request, template_name, {'form': form})
