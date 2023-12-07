from django.db import models
from Movies.models import Movie
# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode





# Create your models here.
class Booking(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    # slug =movie.name.replace(' ' or ':','-')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    theater=models.CharField(max_length=20)
    count=models.IntegerField()
    def __str__(self):
        return self.movie.name

    def qrcode(self):
        # String which represents the QR code
        s = "www.geeksforgeeks.org"
        # Generate QR code
        url = pyqrcode.create(s)
        # Create and save the svg file naming "myqr.svg"
        url.svg("myqr.svg", scale=8)
        # Create and save the png file naming "myqr.png"
        url.png('myqr.png', scale=6)




