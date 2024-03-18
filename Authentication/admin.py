from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'avatar_display')  # Customize displayed fields

    def avatar_display(self, obj):
        return '<img src="%s" style="max-width:100px;max-height:100px" />' % obj.avatar.url
    
    avatar_display.allow_tags = True  # Allow HTML rendering in the admin
    avatar_display.short_description = 'Avatar' 