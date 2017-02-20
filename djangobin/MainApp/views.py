from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def login(request):
    if request.method == "POST":
        #process request object
    else:
        #redirect to loginpage with warning
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=usename,password=password)
    if user is not None:
        login(request,user)
        #redirect to succes age
    else:
        #redirect to login page with error message
        return redirect('/login')
    return render(request,'login.html',{})

@login_required
def logout(request):
    logout(request)
    return redirect('/login/')
