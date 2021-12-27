from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import *
from .tables import *
from django_tables2 import SingleTableView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .repositories import PostRepository

# Create your views here.

class PostListView(LoginRequiredMixin, SingleTableView):
    model = Post
    paginate_by = 10
    table_class = PostTable
    post_repository = PostRepository()
    
    def get_form(self):
        return PostSearchForm(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['search_form'] = self.get_form()
        return context

    def get_queryset(self):
        form = self.get_form()
        return self.post_repository.filter(self.request.user, form.cleaned_data if form.is_valid() else dict())

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    
    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['is_accessible'] = self.object.user.pk == self.request.user.pk
        return self.render_to_response(context)
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.object.user.pk != self.request.user.pk:
            return redirect(self.object.get_absolute_url())
        return self.render_to_response(context)

    def get_form_kwargs(self):
        kwargs = super(PostUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post_list')

