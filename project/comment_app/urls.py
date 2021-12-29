from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('comment/create/<slug:slug>', views.CommentCreateView.as_view(), name='comment_create'),
]
