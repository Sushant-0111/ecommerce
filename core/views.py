from core.serializer import UserSerializer,UserCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view([
    "POST", 
])
def login(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            token,_ =  Token.objects.get_or_create(user=user,)
            return Response(
                {
                    "token": token.key, 
                    "user": user.username,
                }
            )
        return Response({
            "error": "Invalid", 
            "status": status.HTTP_401_UNAUTHORIZED,
        })
        
        
@api_view([
    'POST',
])
def register(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "detail": "User created successfully",
                "status": status.HTTP_201_CREATED,
            }
            )
        
        
        