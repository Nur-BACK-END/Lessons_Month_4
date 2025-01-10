from django.shortcuts import render,HttpResponse
from posts.models import Post



def main_view(request):
    return render(request, "base.html")

def list_view(request):
    posts = Post.objects.all()
    return render(request,"posts_list.html",context={"posts": posts})
