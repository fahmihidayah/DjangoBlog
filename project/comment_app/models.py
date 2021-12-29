from django.db import models
from content_app.models import Post
from account_app.models import UserModel
# Create your models here.


class Comment(models.Model):

    message = models.CharField(max_length=255, default='')

    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now=True)

    updated = models.DateTimeField(auto_now_add=True)
