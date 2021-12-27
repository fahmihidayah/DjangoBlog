from django.db import models
from django_extensions.db.models import AutoSlugField
# Create your models here.
# IGNORE-GENERATE
from django.shortcuts import reverse


class Category(models.Model):
    # READ-ONLY
    slug = AutoSlugField(populate_from='name')

    name = models.CharField(max_length=200, )

    description = models.CharField(max_length=255, )

    # READ-ONLY
    created = models.DateTimeField(auto_now=True)

    # READ-ONLY
    updated = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('category_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('category_update', args=(self.slug,))

    def get_delete_url(self):
        return reverse('post_delete', args=(self.slug,))

    def get_list_url(self):
        return reverse('category_list')

    def get_create_url(self):
        return reverse('category_create')

    def __str__(self):
        return self.name