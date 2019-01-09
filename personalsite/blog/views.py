from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about_me(request):
    return render(request, 'about-me.html')

def blog(request):
    return render(request, 'blog.html')

def curriculum(request):
    return render(request, 'curriculum.html')

def contact(request):
    return render(request, 'contact.html')
