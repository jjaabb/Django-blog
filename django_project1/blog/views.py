from django.shortcuts import render
from django.http import HttpResponse
#creating dummy data

posts = [{'author': 'Algirdas',
'title' : 'Blog Post 1',
'content': 'First post content',
'date_posted':'December 8, 2019'
},
{'author': 'Ernesta',
'title' : 'Blog Post 2',
'content': 'Second post content',
'date_posted':'December 9, 2019'
}]



#Creating function

def home(request):
    '''This function going to handle traffic from the home page of our 
    blog'''
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
