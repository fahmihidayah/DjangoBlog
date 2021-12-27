from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, View
from .forms import SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from category_app.repositories import CategoryRepository

from content_app.repositories import PostRepository
from content_app.models import Post


# Create your views here.

class IndexView(TemplateView):
    post_repository : PostRepository = PostRepository()
    category_repository : CategoryRepository = CategoryRepository()

    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = self.category_repository.find_all()
        category_id = ''

        context['post_banners'] = self.post_repository.find_banner()

        if 'category' in self.request.GET:
            category_id = self.request.GET['category']
            context['selected_category_id'] = category_id

        form = SearchForm(self.request.GET)

        if form.is_valid():
            context['search_form'] = form
            context['posts'] = self.post_repository.filter_published(user=self.request.user,
                                                           params={'title': form.cleaned_data['keyword'],
                                                                    'content': form.cleaned_data['keyword']},
                                                           category=category_id)
        else:
            context['search_form'] = SearchForm()
            context['posts'] = self.post_repository.filter_published(user=self.request.user)



        return context


class FavouriteView(View):
    post_repository : PostRepository = PostRepository()
    login_url = '/login/'
    redirect_field_name = "home"

    def get(self, request, *args, **kwargs):
        return redirect("home")

    def post(self, request, *args, **kwargs):
        print('is user authenticated ' + str(request.user.is_authenticated))
        if request.user.is_authenticated:
            slug = kwargs['slug']
            self.post_repository.favourite_unfavourite(request.user, slug)
        else:
            return redirect('login')
        return redirect("home")

class DetailContentView(DetailView):

    model = Post
    post_repository : PostRepository = PostRepository()
    template_name = "frontend/content_detail.html"
    
    def get_queryset(self):
        return self.post_repository.find_by_slug(self.kwargs['slug'])

