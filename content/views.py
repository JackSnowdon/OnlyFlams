from django.shortcuts import render

# Create your views here.

def content_home(request):
    return render(request, "content_home.html")