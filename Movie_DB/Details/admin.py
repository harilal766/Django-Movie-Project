from django.contrib import admin
from Movies.models import *
from Details.models import *
# Register your models here.
admin.site.register(Award)
admin.site.register(Streaming)
admin.site.register(Certification)
admin.site.register(Genre)