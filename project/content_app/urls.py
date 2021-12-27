from django.urls import path
from .views import *
from .apis import *


urlpatterns = [

    path('post', PostListView.as_view(), name='post_list'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('post/update/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),

    path('api/v1/post', PostListCreateAPIView.as_view() ,name='api_v1_post'),
    path('api/v1/post/<int:pk>', PostRetrieveUpdateDestroyApiView.as_view() ,name='api_v1_detail_post'),

]