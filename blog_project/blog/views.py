from django.shortcuts import render
from rest_framework import generics , status 
from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogPostSerializer
from .models import BlogPost

    
class BlogPostListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print(f'REQUEST DATA: {request.data}')
        blog_post_data = BlogPostSerializer(data=request.data)

        if blog_post_data.is_valid():
            print(f'USER IS {request.user}')
            blog_post_data.save(author=request.user)  
            return Response(blog_post_data.data, status=status.HTTP_201_CREATED)
        
        return Response(blog_post_data.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request):
        blog_post_list = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_post_list,many=True)
        if serializer is not None:
            return Response(serializer.data , status= status.HTTP_200_OK)
        return None
    

class BlogPostView(APIView):

    def get(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"error": "Blog post not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"error": "Blog post not found."}, status=status.HTTP_404_NOT_FOUND)
        
        update_serializer = BlogPostSerializer(blog_post, data=request.data)
        if update_serializer.is_valid():
            update_serializer.save(author=request.user)  # Use request.user for the logged-in user
            return Response(update_serializer.data, status=status.HTTP_200_OK)
        
        return Response(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"error": "Blog post not found."}, status=status.HTTP_404_NOT_FOUND)
        
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

