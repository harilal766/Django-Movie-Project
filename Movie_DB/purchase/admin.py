from django.contrib import admin
from purchase.models import Booking
from Movies.models import Movie
# Register your models here.
# class BookingAdmin(admin.ModelAdmin):
#     list_display=[f'{Booking.movie.name}']
#     prepopulated_fields={'slug':(f'{Booking.movie}',)}
# admin.site.register(Booking,BookingAdmin)


admin.site.register(Booking)

