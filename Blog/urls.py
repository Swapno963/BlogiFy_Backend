from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter() # amader router

router.register('blog/', views.BlogViewset) # router er antena
router.register('comment/', views.CommentViewset) # router er antena
router.register('tag/', views.TagViewset) # router er antena
urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
