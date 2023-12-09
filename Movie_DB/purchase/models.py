from django.db import models
from django.contrib.auth.models import User
from Movies.models import Movie
# Create your models here.
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=30,unique=True)
    qrcode=models.ImageField(upload_to='movies/qrcode')
    theater=models.CharField(max_length=20)
    seats=models.CharField(max_length=20)
    types=models.CharField(max_length=20)
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=10)
    screen=models.CharField(max_length=2)
    booking_id=models.CharField(max_length=10)
    amount=models.IntegerField()
