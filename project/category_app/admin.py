from django.contrib import admin
from .models import *
from .forms import *

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    search_fields = ["slug", "name", "description", "created", "updated"]
    list_display = ["slug", "name", "description", "created", "updated"]
    readonly_fields = [ 'created', 'updated']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
