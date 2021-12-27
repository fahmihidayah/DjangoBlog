from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import *
from .tables import *
from django_tables2 import SingleTableView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .repositories import CategoryRepository

# Create your views here.

class CategoryListView(LoginRequiredMixin, SingleTableView):
    model = Category
    paginate_by = 10
    table_class = CategoryTable
    category_repository = CategoryRepository()
    

    def get_queryset(self):
        
        return self.category_repository.filter()

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category

    def get_success_url(self):
        return reverse('category_list')

