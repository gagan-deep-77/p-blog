from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # body = RichTextField(blank=True,null=True)
    body = HTMLField(default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=now,editable=False)
    def __str__(self):
        return self.title[:20]
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=now,editable=False)
    likes = models.IntegerField(default=0)
    body = models.TextField(max_length=1024)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.body[:64]


