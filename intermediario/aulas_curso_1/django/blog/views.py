from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from blog.data import posts
# Create your views here.

def blog(request:HttpRequest):
    context = {'texto': 'Está no blog', 'posts': posts}
    return render(request, 'blog/index.html', context)


def post(request, _id):
    found_post = None

    for i in posts:
        if i['id'] == _id:
            found_post = i
            break
    
    if found_post is None:
        raise Http404('Post não existe')
    
    context = { 'post': found_post, 'title': found_post['title']}
    return render(request, 'blog/post.html', context)
