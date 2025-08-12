from django.urls import path
from myapp1.views import *

urlpatterns=[
    path('', hello, name='hello'),
    path('hello/<str:helloid>/', helloDetails, name='helloDetails'),
    path('course/', course, name='course'),
    path('course/<int:courseid>', courseDetails, name="courseDetails"),
    path('course/<courseshow>/', courseValue, name='courseValue'),
    path('index/', index, name="index"),
    path('home/', home, name="home"),
    path('post/', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('api/posts/', api_post_list_create, name='api_post_list_create'),
    path('api/posts/<int:pk>/', api_post_detail, name='api_post_detail'),
]