from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RegistrationSerializer,UserLoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

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
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
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
                return Response({'error': 'Invalid credentials'})
        return Response(serializer.errors)