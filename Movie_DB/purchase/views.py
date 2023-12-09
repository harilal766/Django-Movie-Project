from django.shortcuts import render
from purchase.models import Booking
from Movies.models import Movie
import qrcode
# Create your views here.
def booking(request):
    return render(request,'ticketbooking.html')


def book_movie(request,m):
    movie=Movie.objects.get(id=m)
    slug = movie.name.replace('' or ':', '-').lower()
    qr=qrcode.make(f'{movie.name}')
    qr.save(f'{movie.name}, {movie.year}')
    theater=''
    seats=''
    amount=len(seats)
    booking=Booking.objects.create(user=request.user,movie=movie,slug=slug,qrcode=qr,
                                   theater=theater,seats=seats)
    booking.save()
    return render(request,'ticketbooking.html')