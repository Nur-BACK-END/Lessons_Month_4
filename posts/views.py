from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from posts.forms import PostCreateForm
from django.contrib.auth.decorators import login_required

def main_view(request):
    if request.method == 'GET':
        return render(request, "navbar.html")


@login_required(login_url='/login/')
def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/posts_list.html', {'posts': posts})
    


@login_required(login_url='/login/')
def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        return render(request, 'posts/post_detail.html', {'post': post})
    
    

@login_required(login_url='/login/')
def post_create_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        return render(request, 'posts/post_create.html', {'form': form})
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if not form.is_valid():
            return render (request, 'post_create.html', {'form': form})
        elif form.is_valid():

            form.save()
            return redirect('/posts/')

