from django.db import models
from author.models import Author

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    release_date = models.DateField()
    rating = models.IntegerField(default=3,choices=[(1,'1'), (2,'2'), (3, '3'), (4,'4'), (5,'5')])

    def __str__(self):
        return self.name 