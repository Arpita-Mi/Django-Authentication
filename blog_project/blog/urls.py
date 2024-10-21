from django.urls import path
from .views import BlogPostListCreateView , BlogPostView
from .register_login_util import UserRegistrationView, LoginSerializerView


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name = "user_register"),
    path("login/",LoginSerializerView.as_view() ,name = "login_serializer"),
    path('blogposts/', BlogPostListCreateView.as_view(), name= "blog_post_list_create_view"),
    path('blogpost_view/<int:pk>', BlogPostView.as_view(), name="blog_post")

]