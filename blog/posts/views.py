from django.http import  HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import Post


def posts_create(request):
    context = {
        "title": "Create"
    }
    return render(request, "index.html", context)


def posts_detail(request, id=None):
    # instance = Post.objects.get(id=id)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title": "List"
    }
    return render(request,"index.html", context)
    # return HttpResponse("<h1>List</h1>")


def posts_update(request):
    context = {
        "title": "Update"
    }
    return render(request, "index.html", context)


def posts_delete(request):
    context = {
        "title": "Delete"
    }
    return render(request, "index.html", context)