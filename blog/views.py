import json

from django.http import JsonResponse
from django.shortcuts import render

from blog.forms import BlogForm
from blog.models import Blog


# Create your views here.

def index(request):
    form = BlogForm()
    blogs = Blog.objects.all()
    ctx = {'form': form, 'blogs': blogs}
    return render(request, 'blog/index.html', ctx)


def get_blogs(request):
    blogs = Blog.objects.all().values('id', 'title', 'description')
    return JsonResponse({'blogs': list(blogs)}, safe=False)


def create_blog(request):
    body = json.loads(request.body.decode('utf-8'))
    title = body['title']
    description = body['description']
    blog = Blog(title=title, description=description)
    blog.save()
    return JsonResponse({'status': 'success'})


def delete_blog(request, id):
    Blog.objects.get(pk=id).delete()
    return JsonResponse({'status': 'success'})


def edit_blog(request, id):
    body = json.loads(request.body.decode('utf-8'))
    title = body['title']
    description = body['description']
    Blog.objects.filter(pk=id).update(title=title, description=description)
    return JsonResponse({'status': 'success'})
