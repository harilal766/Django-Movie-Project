from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from Crew.models import *
# from Movies.models import Audience_Review
from Details.models import *

class Movie(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True,blank=True)
    year=models.CharField(max_length=5,blank=True)
    language=models.CharField(max_length=50,blank=True)
    release=models.CharField(max_length=100,blank=True)

    rating=models.CharField(max_length=20,blank=True)

    poster=models.ImageField(upload_to='movies/poster',blank=True)
    cover=models.ImageField(upload_to='movies/cover',null=True,blank=True)

    duration=models.CharField(max_length=50,default=None,blank=True)
    streaming=models.ForeignKey(Streaming,on_delete=models.CASCADE,blank=True,null=True)
    ott=models.CharField(max_length=1000,blank=True,null=True)

    actors=models.ManyToManyField(Actor,related_name='actor',blank=True)
    Characters=models.ManyToManyField(Character,related_name='character',blank=True)

    director=models.ForeignKey(Director,on_delete=models.CASCADE,blank=True,null=True)
    writers=models.ManyToManyField(Writer,related_name='writer',blank=True)
    cinematographer=models.ForeignKey(Cinematographer,on_delete=models.CASCADE,null=True,blank=True)

    based =models.CharField(max_length=100,blank=True,null=True)
    genres=models.ManyToManyField(Genre,blank=True)

    certification=models.ForeignKey(Certification,on_delete=models.CASCADE,null=True,blank=True)
    synopsis=models.TextField(max_length=1000,blank=True)
    trailer=models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.name
class Parent(models.Model):
    title=models.CharField(max_length=50,blank=True,null=True)
    slug=models.SlugField(max_length=50,unique=True,default=title)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='user')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    score=models.IntegerField(blank=True,null=True)
    review=models.TextField(max_length=5000,blank=True,null=True)
    class Meta:
        abstract=True
    def __str__(self):
        return self.movie.name,self.title
class Audience_Review(Parent):
    pass







