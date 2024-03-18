from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RegistrationSerializer,UserLoginSerializer,UserProfileSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes)

class UserRegistrationApiView(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): # json data valid hoile er condition e jabe
            user = serializer.save()
            return Response("Form Submission Done")
        return Response(serializer.errors)
      
        
        
class UserLoginApiView(APIView):   
    def post(self, request):
        serializer = UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(email= email, password=password)
            
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "user": {
                        "id": str(user.id),
                        "email": str(user.email),
                        "firstName": str(user.first_name),
                        "lastName": str(user.last_name),
                        "avatar": None,
                        "favourites": []
                    },
                    "token": {
                        "accessToken": str(refresh.access_token),
                        "refreshToken":  str(refresh)
                    }
                }, status=status.HTTP_200_OK)
            
            else:
                return Response({'error': user})
        return Response(serializer.errors)
    
    
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowProfile(APIView):
    def get(self, request, pk):
        try:
            user_profile = User.objects.get(pk=pk)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
