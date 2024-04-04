from rest_framework import serializers
from . import models
from Blog.serializers import BlogSerializer,BlogCommentSerializer
from django.contrib.auth.models import User
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'
        

class UserProfileSerializer(serializers.ModelSerializer):
    BlogUser = BlogCommentSerializer(many=True, read_only=True)
    bio = serializers.CharField(default = '')
    class  Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','BlogUser','bio']
# for registration

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        
        
    def save(self):
        # username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        username = f"{first_name}_{last_name}".lower()
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username=username, email=email, first_name = first_name, last_name = last_name)
        print(' account from registration serializer ',account)
        account.set_password(password)
        account.save()
        return account
    
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['email','password']
       