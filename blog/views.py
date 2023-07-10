from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
        else:
            form = PostForm()
        return render(request, 'blog/post_list.html', {'form':form})


def post_edit(request, pk):
    

# Create your views here.
