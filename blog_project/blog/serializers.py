from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import BlogPost
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password =  serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["username" , "email" , "password"]

    def create(self,validate_data):
        user = User(
            username = validate_data['username'],
            email = validate_data['email']
        )
        user.set_password(validate_data["password"])
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid username or password")

        attrs['user'] = user
        return attrs
    


class BlogPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogPost
        fields = "__all__"