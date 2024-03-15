from django.db import models
from Authentication.models import Author
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
class Comments(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(Author,  on_delete=models.CASCADE)

    
class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=500)
    thumbnail = models.FileField(upload_to='blog_img/')
    author = models.ForeignKey(Author,  on_delete=models.CASCADE,related_name='blog_author')
    tag = models.ManyToManyField(Tag)
    likes = models.IntegerField()
    comments = models.ForeignKey(Author,  on_delete=models.CASCADE,related_name='blog_commentor')