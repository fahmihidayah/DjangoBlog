from django.db import models
from account_app.models import UserModel
from category_app.models import Category
from django_extensions.db.models import AutoSlugField
# Create your models here.
from django.urls import reverse
from django.contrib.flatpages.models import FlatPage
import os
from tinymce import models as tinymce_models
# IGNORE-GENERATE

class Post(models.Model):
    # READ-ONLY
    slug = AutoSlugField(populate_from='title')

    image = models.ImageField(upload_to='post/%Y-%m-%d', default='img_placeholder.png')

    # SEARCH
    title = models.CharField(max_length=255,)
    # SEARCH
    content = tinymce_models.HTMLField()

    categories = models.ManyToManyField(to=Category)

    users_liked = models.ManyToManyField(to=UserModel, related_name='users')

    # CURRENT-USER
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    is_published = models.BooleanField(default=True)

    is_banner = models.BooleanField(default=False)

    # READ-ONLY
    created = models.DateTimeField(auto_now=True)

    # READ-ONLY
    updated = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('post_update', args=(self.slug,))

    def get_delete_url(self):
        return reverse('post_delete', args=(self.slug,))

    def get_list_url(self):
        return reverse('post_list')

    def get_create_url(self):
        return reverse('post_create')

    def get_image_url(self):

        return os.path.join('/media', self.image)

