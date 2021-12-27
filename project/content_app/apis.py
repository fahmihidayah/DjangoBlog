from rest_framework import generics
from .serializers import  PostSerializer
from .repositories import PostRepository
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from project.api_utils import get_response


class PostListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    serializer_class = PostSerializer
    post_repository = PostRepository()

    def get_queryset(self):
        return self.post_repository.filter(self.request.user,self.request.GET.dict())

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super(PostListCreateAPIView, self).list(request, *args, **kwargs)
        return get_response(data=response.data)

    def create(self, request, *args, **kwargs):
        response = super(PostListCreateAPIView, self).create(request, *args, **kwargs)
        return get_response(data=response.data)


class PostRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    serializer_class = PostSerializer
    post_repository = PostRepository()

    def get_queryset(self):
        return self.post_repository.filter(self.request.user,self.request.GET.dict())

    def retrieve(self, request, *args, **kwargs):
        response = super(PostRetrieveUpdateDestroyApiView, self).retrieve(request, *args, **kwargs)
        return get_response(data=response.data)

    def delete(self, request, *args, **kwargs):
        response = super(PostRetrieveUpdateDestroyApiView, self).delete(request, *args, **kwargs)
        return get_response(data=response.data)

    def update(self, request, *args, **kwargs):
        response = super(PostRetrieveUpdateDestroyApiView, self).update(request, *args, **kwargs)
        return get_response(data=response.data)



