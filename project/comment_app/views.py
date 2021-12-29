from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from .models import Comment
from .forms import CommentForm
from content_app.repositories import PostRepository
# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    post_repository : PostRepository = PostRepository()

    def get_success_url(self):
        return reverse('view_post_detail', kwargs={'slug': self.object.post.slug})

    def get_form(self, form_class=None):
        form = super(CommentCreateView, self).get_form(form_class=form_class)
        form.user = self.request.user
        form.post = self.post_repository.get_by_slug(slug=self.kwargs['slug'])
        return form





