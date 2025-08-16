from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from myapp1.models import Post
from myapp1.forms import PostForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp1.serializers import PostSerializer


# Create your views here.

def hello(request):
    return HttpResponse("hello, sam")

def helloDetails(request,helloid):
    return HttpResponse(helloid)

def course(request):
    return HttpResponse("these are details related to course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def courseValue(request,courseshow):
    return HttpResponse(courseshow)

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")


# read(list)
def post_list(request):
    posts = Post.objects.all()
    return render(request,"post_list.html",{"posts":posts})


# read(single)
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,"post_detail.html",{"post":post})


#create
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request,"post_form.html",{"form":form})


#update
def post_update(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form=PostForm(instance=post)
    return render(request,"post_form.html",{"form":form})


#delete
def post_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect("post_list")


@api_view(['GET', 'POST'])

def api_post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)