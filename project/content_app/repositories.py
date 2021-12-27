from .models import *
from django.db import models


class PostRepository:
    
    def find(self, user) -> models.QuerySet:
        if user:
            return Post.objects.annotate(
                is_favourite=models.Count('users_liked', filter=models.Q(users_liked__id=user.id)))\
                .filter(models.Q(is_banner=False))
        else:
            return Post.objects.filter(models.Q(is_banner=False))
        
    def filter(self, user, params: dict= None, category: str = None) -> models.QuerySet:
        query_set = self.find(user)
        if user:
            query_set = query_set.filter(user=user)
        if params:
            query_set = query_set.filter(models.Q(title__icontains=params.get('title', '')) | models.Q(content__icontains=params.get('content', '')))
        if category:
            query_set = query_set.filter(categories__id=category)
        return query_set

    def count(self):
        return Post.objects.all().count()

    def find_all(self, user = None):
        return Post.objects.annotate(is_favourite=models.Count('users_liked', filter=models.Q(users_liked_id=user.id))).all()

    def find_by_slug(self, slug, user = None):
        return self.find(user).filter(slug=slug)

    def get_by_slug(self, slug, user = None):
        return self.find(user).get(slug=slug)

    def filter_published(self, user = None, params : dict = None, category : str = None):
        query_set = self.find(user).filter(models.Q(is_published=True))
        if params:
            query_set = query_set.filter(models.Q(title__icontains=params.get('title', '')) | models.Q(content__icontains=params.get('content', '')))
        if category:
            query_set = query_set.filter(categories__id=category)
        return query_set

    def is_users_liked_contain(self, slug, user):
        count = Post.objects.filter(models.Q(slug=slug) & models.Q(users_liked__id=user.id)).count()
        return count == 1

    def favourite(self, user, slug):
        post : Post = self.get_by_slug(slug=slug, user=user)
        post.users_liked.add(user)

    def unfavourite(self, user, slug):
        post : Post = self.get_by_slug(slug=slug, user=user)
        post.users_liked.remove(user)

    def favourite_unfavourite(self, user, slug):
        post: Post = self.get_by_slug(slug)
        if self.is_users_liked_contain(slug=slug, user=user):
            self.unfavourite(user, slug)
        else:
            self.favourite(user, slug)
        return post

    def find_banner(self):
        return Post.objects.filter(models.Q(is_banner=True))