from rest_framework import serializers
from django.contrib.auth import get_user_model 



User  = get_user_model()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    
    
    
class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                    "confirm_password": "Confirm Passwords must match with password.", 
                })
        return attrs
    
    
    def create(self, validate_data):
        validate_data.pop('confirm_password')
        return User.objects.create_user(**validate_data)
        