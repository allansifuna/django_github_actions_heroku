from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts=[{
    'title':'Blog 1',
    'author':'Allan Sifuna',
    'content':'This is the first post',
    'date_posted':'Aug 13 2019'
    },{
    'title':'Blog 2',
    'author':'Allan Sifuna',
    'content':'This is the Second post',
    'date_posted':'Aug 13 2019'
    },{
    'title':'Blog 3',
    'author':'Allan Sifuna',
    'content':'This is the Third post',
    'date_posted':'Aug 13 2019'
    }
    ]
# Create your views here.
def home(request):
    data={'posts':Post.objects.all()}
    return render(request,'blog/home.html',data)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
