from django.shortcuts import render
from album.forms import Album
def home(req):
    data = Album.objects.all()
    print(data)
    return render(req, 'home.html', {'data': data})