from django.urls import path
from listings.views import home

urlpatterns = [
    path('',home,name='blog-home')
]
