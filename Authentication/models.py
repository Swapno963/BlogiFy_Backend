from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=500)
    avatar = models.FileField(upload_to='blog_img/')
    
    def __str__(self) -> str:
        return self.firstName
