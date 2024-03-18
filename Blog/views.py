from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import generics

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100
    
    
class BlogViewset(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    # @action(detail=True, methods=['post'])
    def toggle_like(self, request,pk=None):
        blog_post = self.get_object()
        blog_post.likes += 1
        blog_post.save()
        return Response({'Count': blog_post.likes})
    
    
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def most_popular(self, request):
        most_popular_post = models.Blog.objects.order_by('-likes')[:2]
        serializer = serializers.BlogSerializer(most_popular_post,many=True)
        return Response(serializer.data)
    
    
from rest_framework.decorators import action
from rest_framework.response import Response    
class BlogPostViewSet2(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogPostSerializer

    @action(detail=False, methods=['post'])
    def create_blog_post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CommentPostViewSet(viewsets.ModelViewSet):
    queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentUsSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        blog_post_id = kwargs.get('pk')
        # print(blog_post_id)
        try:
            blog_post = models.Blog.objects.get(id=blog_post_id)
        except models.Blog.DoesNotExist:
            return Response({'error': 'Blog post does not exist.'})

        serializer = serializers.CommentUsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # serializer.save(blog_post=blog_post, commenter=request.user)

        return Response({'success': True, 'data': serializer.data})
# class CommentViewset(viewsets.ModelViewSet):
#     queryset = models.Comments.objects.all()
#     serializer_class = serializers.CommentUsSerializer

class TagViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] 

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagUsSerializer
    
    
# class BlogSearchView(generics.ListAPIView):
#     queryset = models.Blog.objects.all()
#     serializer_class = serializers.BlogSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title']
