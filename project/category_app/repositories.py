from .models import *
from django.db import models

class CategoryRepository:

    def filter(self, ):
        query_set = Category.objects.all()
        return query_set

    def find_all(self):
        return Category.objects.all()
