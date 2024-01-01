from django.shortcuts import render
from . import forms

# Create your views here.
def add_author(req):
    author_form = forms.authorForm()
    return render(req, 'author.html',{'form': author_form})