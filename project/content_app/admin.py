from django.contrib import admin
from .models import *
from .forms import *

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    search_fields = ["slug", "title", "user", "is_published", "created", "updated"]
    list_display = ["slug", "title", "user", "is_published", "created", "updated"]
    readonly_fields = [ 'created', 'updated']

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, change, **kwargs)
        form.user = request.user
        return form

# Register your models here.
admin.site.register(Post, PostAdmin)
