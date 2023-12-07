from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display=['movie']
    prepopulated_fields={'slug':('movie',)}
admin.site.register(Booking,BookingAdmin)


