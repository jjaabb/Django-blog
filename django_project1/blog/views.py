from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

#Creating function

def home(request):
    '''This function going to handle traffic from the home page of our 
    blog'''
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})