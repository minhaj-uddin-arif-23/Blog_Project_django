from django.shortcuts import render,redirect
from Post.models import post
def home(request):
    data = post.objects.all()
    return render(request,'home.html',{'data':data})