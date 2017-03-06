from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from datetime import datetime
#forms
from .form import NewPost, LoginForm, SignUpForm
# Modals
from .models import Post
# Create your views here.

def home_old(request):
    context_pass = {
        'form':NewPost
    }
    return render(request,'home.html',context_pass)


class all_posts(ListView):
    model = Post
    template_name = 'all-posts.html'
    context_object_name = 'all_posts'

class base_view(ListView):
    queryset = Post.objects.all()
    # template_name = 'home.html'
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(base_view, self).get_context_data(**kwargs)
        #Add in a QuerySet of all the books
        current_user = self.request.user
        if current_user.is_authenticated:
            context_user = current_user
        else:
            context_user = get_object_or_404(Post,id=1)

        print(current_user)
        context['form'] = NewPost(initial={'writer': context_user,'timestamp':datetime.now()})
        context['latest_posts'] = Post.objects.all().order_by("-timestamp")[:15]
        context['custom_objects'] = Post.objects.all().order_by("-timestamp")
        return context


class post_detail_view(DetailView):
    model = Post
    context_object_name = 'thisPost'
    def get_context_data(self, **kwargs):
        context = super(post_detail_view, self).get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all().order_by("-timestamp")[:15]
        return context

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
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request, "Hi,%s ! You have been Succesfully Signed Up, Please Login Again " % (firstname))
    return redirect("MainApp:login")


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

    return redirect("MainApp:login")



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out Succesfully")
    return HttpResponseRedirect('/login/')


def post_form_upload(request):
    print(request.POST)
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            form.timestamp = datetime.now()
            print(form)
            form.save()
            return redirect("MainApp:home")
    else:
        messages.success(request, "form not saved due to error")
    return redirect("MainApp:home")



def single_post(request):
    return render(request,'single-post.html',{})

def single_user(request):
    return render(request,'single-user.html',{})

