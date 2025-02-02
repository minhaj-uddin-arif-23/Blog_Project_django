from django.shortcuts import render,redirect
from . import forms

def add_author(request):
    if request.method == "POST":
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = forms.AuthorForm()
    return render(request,'./author/add_author.html',{'form':author_form}) 