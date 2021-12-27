from django.urls import path
from .views import *
from .apis import *


urlpatterns = [

    path('category', CategoryListView.as_view(), name='category_list'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug:slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<slug:slug>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<slug:slug>', CategoryDeleteView.as_view(), name='category_delete'),

    path('api/v1/category', CategoryListCreateAPIView.as_view() ,name='api_v1_category'),
    path('api/v1/category/<int:pk>', CategoryRetrieveUpdateDestroyApiView.as_view() ,name='api_v1_detail_category'),

]