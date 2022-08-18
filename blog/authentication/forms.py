from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

input_class = "border text-2xl p-4 hover:outline-slate-500  focus:ring focus:ring-orange-200"

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
