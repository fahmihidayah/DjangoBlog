from rest_framework import generics
from .serializers import  CategorySerializer
from .repositories import CategoryRepository
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from project.api_utils import get_response


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    serializer_class = CategorySerializer
    category_repository = CategoryRepository()

    def get_queryset(self):
        return self.category_repository.filter()

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        response = super(CategoryListCreateAPIView, self).list(request, *args, **kwargs)
        return get_response(data=response.data)

    def create(self, request, *args, **kwargs):
        response = super(CategoryListCreateAPIView, self).create(request, *args, **kwargs)
        return get_response(data=response.data)


class CategoryRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    serializer_class = CategorySerializer
    category_repository = CategoryRepository()

    def get_queryset(self):
        return self.category_repository.filter()

    def retrieve(self, request, *args, **kwargs):
        response = super(CategoryRetrieveUpdateDestroyApiView, self).retrieve(request, *args, **kwargs)
        return get_response(data=response.data)

    def delete(self, request, *args, **kwargs):
        response = super(CategoryRetrieveUpdateDestroyApiView, self).delete(request, *args, **kwargs)
        return get_response(data=response.data)

    def update(self, request, *args, **kwargs):
        response = super(CategoryRetrieveUpdateDestroyApiView, self).update(request, *args, **kwargs)
        return get_response(data=response.data)



