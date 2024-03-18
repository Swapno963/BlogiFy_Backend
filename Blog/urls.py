from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter() # amader router

router.register('blog', views.BlogViewset) # for normal blog
# router.register('blogPost', views.BlogPostViewSet) # router er antena
router.register('blogPost2', views.BlogPostViewSet2) # router er antena
# router.register('comment', views.CommentViewset) # router er antena
router.register('tag', views.TagViewset) # router er antena
# router.register('popular', views.PopularBlogViewSet) # router er antena
urlpatterns = [
    path('', include(router.urls)),
    path('popular/', views.BlogPostViewSet.as_view({'get': 'most_popular'}), name='most_popular'),
    path('like/<int:pk>/', views.BlogViewset.as_view({'get': 'toggle_like'}), name='toggle_like'),
    
    path('comment/<int:pk>/', views.CommentPostViewSet.as_view({'post': 'create'})),
    # path('blogPost2', views.BlogPostViewSet2.as_view({'post': 'create_blog_post'})),

]
