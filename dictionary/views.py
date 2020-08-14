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

def detail(request):
    posts2 = Post.objects.all()

    return render(
        request,
        'dictionary/detail.html',
        {
            'posts2': posts2,
        }
    )

def detail2(request):
    posts3 = Post.objects.all()

    return render(
        request,
        'dictionary/detail2.html',
        {
            'posts3': posts3,
        }
    )

def detail3(request):
    posts4 = Post.objects.all()

    return render(
        request,
        'dictionary/detail3.html',
        {
            'posts4': posts4,
        }
    )

def detail4(request):
    posts5 = Post.objects.all()

    return render(
        request,
        'dictionary/detail4.html',
        {
            'posts5': posts5,
        }
    )

def detail5(request):
    posts6 = Post.objects.all()

    return render(
        request,
        'dictionary/detail5.html',
        {
            'posts6': posts6,
        }
    )

def detail6(request):
    posts7 = Post.objects.all()

    return render(
        request,
        'dictionary/detail6.html',
        {
            'posts7': posts7,
        }
    )

def detail7(request):
    posts8 = Post.objects.all()

    return render(
        request,
        'dictionary/detail7.html',
        {
            'posts8': posts8,
        }
    )

def detail8(request):
    posts9 = Post.objects.all()

    return render(
        request,
        'dictionary/detail8.html',
        {
            'posts9': posts9,
        }
    )

def detail9(request):
    posts10 = Post.objects.all()

    return render(
        request,
        'dictionary/detail9.html',
        {
            'posts10': posts10,
        }
    )

def detail10(request):
    posts11 = Post.objects.all()

    return render(
        request,
        'dictionary/detail10.html',
        {
            'posts11': posts11,
        }
    )

def detail11(request):
    posts12 = Post.objects.all()

    return render(
        request,
        'dictionary/detail11.html',
        {
            'posts12': posts12,
        }
    )

def detail12(request):
    posts13 = Post.objects.all()

    return render(
        request,
        'dictionary/detail12.html',
        {
            'posts13': posts13,
        }
    )

def detail13(request):
    posts14 = Post.objects.all()

    return render(
        request,
        'dictionary/detail13.html',
        {
            'posts14': posts14,
        }
    )

def detail14(request):
    posts15 = Post.objects.all()

    return render(
        request,
        'dictionary/detail14.html',
        {
            'posts15': posts15,
        }
    )

def detail15(request):
    posts16 = Post.objects.all()

    return render(
        request,
        'dictionary/detail15.html',
        {
            'posts16': posts16,
        }
    )

def detail16(request):
    posts17 = Post.objects.all()

    return render(
        request,
        'dictionary/detail16.html',
        {
            'posts17': posts17,
        }
    )

def detail17(request):
    posts18 = Post.objects.all()

    return render(
        request,
        'dictionary/detail17.html',
        {
            'posts18': posts18,
        }
    )