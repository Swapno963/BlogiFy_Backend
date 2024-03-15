from rest_framework import serializers
from . import models

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'
class CommentUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = '__all__'
class TagUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'