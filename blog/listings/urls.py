from django.urls import path,include
from listings.views import home , create_blog , posts , blog_detail
from rest_framework.routers import SimpleRouter
from listings.views import PostApi

router =  SimpleRouter()

router.register('posts',PostApi,basename='api-posts')

urlpatterns = [
    path('home',home,name='blog-home'),
    path('posts/create/',create_blog,name='blog-post-create'),
    path('posts/',posts, name='blog-all-posts'),
    path('api/',include(router.urls)),
    path('posts/<int:id>',blog_detail,name='blog-detail')
]
