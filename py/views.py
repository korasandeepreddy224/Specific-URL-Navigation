from django.shortcuts import render

# Create your views here.
def cat(request):
    return render(request,'cat.html')