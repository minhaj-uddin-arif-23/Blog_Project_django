from django.shortcuts import render
from . import forms

def add_author(request):
    author_form = forms.AuthorForm()
    return render(request,'./author/add_author.html',{'form':author_form}) 