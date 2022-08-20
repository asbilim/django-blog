from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)  
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.title + '\n' + self.description
