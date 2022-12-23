from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from blog.views import index, get_blogs, create_blog, delete_blog

urlpatterns = [
    path('', index, name='index'),
    path('blogs/', get_blogs, name='blogs'),
    path('create/', csrf_exempt(create_blog), name='create'),
    path('delete/<id>/', csrf_exempt(delete_blog), name='delete'),
]
