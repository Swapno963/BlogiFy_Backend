from rest_framework import serializers
from . import models

class BlogSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.firstName')
    # comments = serializers.ReadOnlyField()
    # tag = serializers.ReadOnlyField(many=True)

    class Meta:
        model = models.Blog
        fields = ['id','author','title','comments','thumbnail','content','tag','likes']
        
    
    
    
class CommentUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = '__all__'
class TagUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'