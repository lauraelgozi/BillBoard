from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Posts(models.Model):
    user = models.ForeignKey(User)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    visible = models.BooleanField(default=True)
    



class Comments(models.Model):
    post_id = models.ForeignKey(Posts, on_delete = models.CASCADE)
    text_comment = models.TextField()
    visible = models.BooleanField(default=True)






