from django.shortcuts import render,redirect
from .forms import  PostForm
from .models import Post

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

