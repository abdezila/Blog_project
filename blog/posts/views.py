from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    Posts = Post.objects.all()
    return render(request, 'index.html', {'Posts': Posts})

def post(request,pk):
    posts = Post.objects.get(id = pk)
    return render(request,'Posts.html',{'posts':posts})

def about(request):
    return render(request,'about.html')