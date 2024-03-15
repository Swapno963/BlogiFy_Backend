from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('',views.getRoutes),
    path('register/',views.UserRegistrationApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('profile/',views.ProfileAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
