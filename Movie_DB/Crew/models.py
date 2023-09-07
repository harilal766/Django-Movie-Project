from django.db import models
# Create your models here.
class Parent(models.Model):
    name=models.CharField(max_length=30,unique=True,default=None)
    slug=models.SlugField(max_length=50,unique=True)
    designation=models.CharField(max_length=30,blank=True)
    about=models.TextField(max_length=2000,blank=True,null=True)
    class Meta:
        abstract = True
    def __str__(self):
        return self.name
class Actor(Parent):
    photo=models.ImageField(upload_to='crew/actor',blank=True,null=True)
class Character(models.Model):
    name=models.CharField(max_length=30,unique=True,default=None)
    def __str__(self):
        return self.name

class Director(Parent):
    photo=models.ImageField(upload_to='crew/director',blank=True,null=True)

class Writer(Parent):
    photo=models.ImageField(upload_to='crew/writer',blank=True,null=True)

class Cinematographer(Parent):
    photo=models.ImageField(upload_to='crew/cinematographer',blank=True,null=True)

