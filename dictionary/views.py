from django.shortcuts import render
from . models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'dictionary/index.html',
        {
            'posts': posts,
        }
    )

def post_detail(request, pk):
    dictionary_post = Post.objects.get(pk=pk)

    return render(
        request,
        'dictionary/post_detail.html',
        {
            'dictionary_post': dictionary_post,
        }
    )