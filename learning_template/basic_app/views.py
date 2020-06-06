from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def relative(request):
    return render(request,'basic_app/relative_tagging.html')

def other(request):
    return render(request,'basic_app/other.html')
