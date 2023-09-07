from django.db import models
from django.contrib.auth.models import User
from Movies.models import Movie

# Create your models here.
class Watchlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.movie.name
