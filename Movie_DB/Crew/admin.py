from django.contrib import admin
from Crew.models import *

# Register your models here.
admin.site.register(Character)

class Admin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        abstract = True
class ActorAdmin(Admin):
    pass
admin.site.register(Actor, ActorAdmin)
class DirectorAdmin(Admin):
    pass
admin.site.register(Director,DirectorAdmin)
class WriterAdmin(Admin):
    pass
admin.site.register(Writer,WriterAdmin)
class CinematographerAdmin(Admin):
    pass
admin.site.register(Cinematographer,CinematographerAdmin)


