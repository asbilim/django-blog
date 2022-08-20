from django.urls import path
from listings.views import home , create_blog

urlpatterns = [
    path('home',home,name='blog-home'),
    path('posts/create/',create_blog,name='blog-post-create')
]
