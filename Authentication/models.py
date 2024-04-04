from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=500)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    avatar = models.FileField(upload_to='blog_img/')
    
    def __str__(self) -> str:
        return f'{self.firstName} {self.lastName}'
    
