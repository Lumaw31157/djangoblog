from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'blog/about.html', {'content': 'My Blog'})

def contact(request):
    return render(request,'blog/contact.html',{'Mynumber': 'Welcome'} )
