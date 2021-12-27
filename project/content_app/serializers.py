from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['pk', "slug", "title", "content", "user", "is_published", "created", "updated", ]
