from django.shortcuts import render,redirect
from django.contrib.auth import login
from . forms import RegisterForm

def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('blog-home')
        return render(request,form)


    return render(request,'authentication/register.html',{'form':form})
