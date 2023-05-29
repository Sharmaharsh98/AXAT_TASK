from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
# from .decorators import unauthenticated_user
from django.contrib.auth.models import Group


email = 0


# Create your views here.
def Signup_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # group = Group.objects.get(name='STUDENT')
            # user.groups.add(group)

            return redirect('login')
    template_name = 'auth_app/Signup.html'
    context = {'form':form}
    return render(request, template_name, context)

def Login_view(request):
    template_name = 'auth_app/Login.html'
    context = {}
    if request.method == "POST":
        global email
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email),'====>', print(password)

        user = authenticate(email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, template_name, context)

def Logout_view(request):
    logout(request)
    return redirect('login')