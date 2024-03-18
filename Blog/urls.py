from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter() # amader router
router.register('blog', views.BlogViewset , basename='blogpost1') 

router2 = DefaultRouter()
router2.register('blogPost2', views.BlogPostViewSet2 , basename='blogpost2') 

router3 = DefaultRouter()
router3.register('tag', views.TagViewset, basename='blogpost3') 
urlpatterns = [
    path('', include(router.urls)),
    path('popular/', views.BlogPostViewSet.as_view({'get': 'most_popular'}), name='most_popular'),
    path('like/<int:pk>/', views.BlogViewset.as_view({'get': 'toggle_like'}), name='toggle_like'),
    
    path('comment/<int:pk>/', views.CommentPostViewSet.as_view({'post': 'create'})),
    # path('blogPost2', views.BlogPostViewSet2.as_view({'post': 'create_blog_post'})),

]
