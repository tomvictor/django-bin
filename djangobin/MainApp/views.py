from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
#forms
from .form import NewPost, LoginForm, SignUpForm
# Create your views here.

def home(request):
    context_pass = {
        'form':NewPost
    }
    return render(request,'home.html',context_pass)

def login(request):
    context_pass = {
        'form': LoginForm,
        'page_title': "Please Sign In",
        'pageurl':"login"
    }
    return render(request,'login.html',context_pass)

def sign_up_view(request):
    context_pass = {
        'form': SignUpForm,
        'page_title': "Register Now",
        'pageurl': "signup"
    }
    return render(request,'login.html',context_pass)

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            firstname = form.cleaned_data.get("firstname")
            lastname = form.cleaned_data.get("lastname")
            user = User.objects.create_user(username, username, password)
    return redirect("mainSiteApp:LoginPage")


def login_form(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        loginpassword = request.POST.get("password")
        # print(username)
        # print(loginpassword)
        # messages.success(request, "printed post data sussesfully\n" + username +"\n" + request.POST.get("loginpassword") )
        user = authenticate(username=username, password=loginpassword)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, "You have been securely logged in")
                return redirect("MainApp:home")
            else:
                messages.success(request, "The password is valid, but the account has been disabled!"
                                          " Please contact us, mail : tom@technorip.com")
                return redirect("MainApp:login")
        else:
            messages.success(request, "The username and password were incorrect,or you may not activated.check your mail for activation link ")
            return redirect("MainApp:login")

    return redirect("mainSiteApp:LoginPage")



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out Succesfully")
    return HttpResponseRedirect('/login/')


def single_post(request):
    return render(request,'single-post.html',{})

def single_user(request):
    return render(request,'single-user.html',{})

def all_pastes(request):
    return render(request,'all-posts.html',{})
