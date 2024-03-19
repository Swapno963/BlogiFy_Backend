from django.contrib import admin
from .models import Tag,Comments,Blog,BlogLover
# Register your models here.
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Blog)
admin.site.register(BlogLover)
