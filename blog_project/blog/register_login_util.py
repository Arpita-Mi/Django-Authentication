from rest_framework import generics , status 
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer , LoginSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "User Register Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginSerializerView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)   
        if serializer.is_valid():
            user = serializer.validated_data['user']  
            refresh = RefreshToken.for_user(user)  
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id' : str(user.id)
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)