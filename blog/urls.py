from django.urls import path

from blog.views import index, get_blogs

urlpatterns = [
    path('', index, name='index'),
    path('blogs/', get_blogs, name='blogs'),
]
