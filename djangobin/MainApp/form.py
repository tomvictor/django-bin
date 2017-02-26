from django import forms
from django.forms.widgets import Textarea,RadioSelect
from MainApp.models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =[
            "title",
            "content",
            "status"
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
                'max_length': "This writer's name is too long.",
            },
        }


        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 13}),
            'status' : RadioSelect
        }