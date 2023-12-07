from django.shortcuts import render
from .models import Booking
# Create your views here.

def add_booking(request):
    return render(request,'ticketbooking.html')
