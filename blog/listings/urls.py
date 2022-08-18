from django.urls import path
from listings.views import home

urlpatterns = [
    path('home',home,name='blog-home')
]
