from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from . import models
from . import serializers

class BlogViewset(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentUsSerializer

class TagViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] 

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagUsSerializer