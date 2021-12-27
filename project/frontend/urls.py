from django.urls import path
from .views import IndexView, DetailContentView, FavouriteView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('', IndexView.as_view(), name='index'),
    path('view_post/<slug:slug>', DetailContentView.as_view(), name='view_post_detail'),
    path('favourite_post/<slug:slug>', FavouriteView.as_view(), name='favourite_post'),
]