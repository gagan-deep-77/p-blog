from django.forms import ModelForm, fields
from .models import User,Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title","body")