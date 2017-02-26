from django import forms
from django.forms import Textarea
from MainApp.models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =[
            "title",
            "content",
            "status"
        ]
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 15}),
        }