from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello welcome to home page")
    return render(request,'index.html')
def about(request):
    return HttpResponse("hello welcome to about page")
def contact(request):
    return HttpResponse("hello you are welcome to contact page")
