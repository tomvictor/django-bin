from django import forms
from django.forms.widgets import Textarea,RadioSelect
from MainApp.models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =[
            "title",
            "content",
            "image",
            "files",
            "status",
            "writer",
            "timestamp"
        ]
        labels = {
            'title': 'Title',
            'content': 'Content'
        }


        help_texts = {
            'status' : 'Please login for Private posts'
        }

        error_messages = {
            'title': {
                'max_length': "This title is too long.",
            },
        }


        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 10,'class':'tinymce'}),
            'status' : RadioSelect,
            'writer' : forms.HiddenInput(),
            'timestamp': forms.HiddenInput(),
        }

class LoginForm(forms.Form):
    username = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember = forms.BooleanField(label="Remember Me",required=False )


class SignUpForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    username = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)