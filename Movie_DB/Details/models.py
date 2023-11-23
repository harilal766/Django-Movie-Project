from django.db import models
# from movie.models import Movie
from django.contrib.auth.models import User
# Create your models here.

class Parent(models.Model):
    name=models.CharField(max_length=100,blank=True,default=None)
    class Meta:
        abstract = True
    def __str__(self):
        return self.name
class Award(Parent):
    logo=models.ImageField(upload_to='award',blank=True)
class Streaming(Parent):
    logo=models.ImageField(upload_to='streaming/logo',blank=True,null=True)
class Certification(Parent):
    pass
class Genre(Parent):
    pass

