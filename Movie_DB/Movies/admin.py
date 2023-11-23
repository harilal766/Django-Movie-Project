from django.contrib import admin
from Movies.models import *

# Register your models here.
# admin.site.register(Movie)

class Movieadmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Movie,Movieadmin)

admin.site.register(Audience_Review)

