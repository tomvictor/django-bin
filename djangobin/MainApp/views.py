from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def login(request):
    return render(request,'login.html',{})

def login_form(request):
    if request.method == 'POST':
        username = request.POST.get("email")
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
                                          " Please contact us, mail : bosch@makervillage.in")
                return redirect("MainApp:login")
        else:
            messages.success(request, "The username and password were incorrect,or you may not activated.check your mail for activation link ")
            return redirect("MainApp:login")

    return redirect("mainSiteApp:LoginPage")


@login_required
def logout(request):
    logout(request)
    return redirect('/login/')


def single_post(request):
    return render(request,'single-post.html',{})

def single_user(request):
    return render(request,'single-user.html',{})
