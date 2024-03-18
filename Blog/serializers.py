from rest_framework import serializers
from . import models


class CommentUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = '__all__'
        
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = ['user','title','content','tag','thumbnail','likes']
        # fields = '__all__'

            
            
            
class BlogSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.firstName')
    # comments = serializers.ReadOnlyField()
    # tag = serializers.ReadOnlyField(many=True)
    comment_writer = CommentUsSerializer(many=True, read_only=True)
    class Meta:
        model = models.Blog
        fields = ['id','title','thumbnail','content','tag','likes','createdAt','comment_writer']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Customize the representation if needed
        data['user'] = str({
            'id':instance.user.id,
            'firstName':instance.user.first_name,
            'lastName':instance.user.last_name,
            # 'avatar':""
        })
        return data
    
class BlogCommentSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.firstName')
    # comments = serializers.ReadOnlyField()
    # tag = serializers.ReadOnlyField(many=True)
    # comment_writer = CommentUsSerializer(many=True, read_only=True)
    class Meta:
        model = models.Blog
        fields = ['id','title','thumbnail','content','tag','likes','user','createdAt']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Customize the representation if needed
        data['author'] = str({
            'id':instance.user.id,
            'firstName':instance.user.first_name,
            'lastName':instance.user.last_name,
            # 'avatar':instance.author.avatar
        })
        return data   
  
class TagUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'