from django.shortcuts import render
from .models import userData
from .forms import userForm

# Create your views here.

def homepage(request):
    return render(request,template_name='base/main.html')


def reachUs(request):
    form=userForm
    return render(request,template_name='base/reachUs.html',context={'form':form})