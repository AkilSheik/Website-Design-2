from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Website_Design"""
    return render(request, 'Website_Design/index.html')
def about(request):
    return render(request, 'Website_Design/about.html')



