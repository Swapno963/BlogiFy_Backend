from django.db import models
from Authentication.models import Author
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


    
class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=500)
    thumbnail = models.FileField(upload_to='blog_img/',null=True, blank=True)
    # author = models.ForeignKey(Author,  on_delete=models.CASCADE,related_name='blog_author')
    tag = models.ManyToManyField(Tag)
    likes = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    # userLikes = models.ManyToManyField(Author, related_name='liked_posts', blank=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='BlogUser')
    
    def __str__(self) -> str:
        return self.title
    
    
class Comments(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,  on_delete=models.CASCADE, null= True, blank=True,related_name='comment_writer')
    def __str__(self) -> str:
        return self.content