from django.shortcuts import render,redirect
from .forms import  PostForm
from .models import Post
from listings.serializer import PostSerializer
from rest_framework.viewsets import ModelViewSet

def home(request):

    return render(request,'listings/home.html')


def create_blog(request):

    if not request.user.is_authenticated:
        return redirect('blog-home')

    form = PostForm

    if request.method == "POST":

        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            author = request.user
            Post.objects.create(title=title , description=description , author=author)
            return redirect('blog-home')
    return render(request,'listings/create.html',{'form':form})



def posts(request):

    posts = Post.objects.all()
    return render(request,'listings/blogs.html',{'post':posts})

def blog_detail(request,id):

    try:
        blog = Post.objects.get(id=id)
        calling = blog.author
        if blog.author == request.user:
            calling = "you"

    except :
        return redirect('blog-home')

    return render(request,'listings/detail.html',{'blog':blog,'calling':calling})

class PostApi(ModelViewSet):

    serializer_class = PostSerializer

    def get_queryset(self):
        
        return Post.objects.all()

