from django.contrib import admin
from django.urls import path,include
from Crew import views
app_name='Crew'
urlpatterns=[
    path('view_actor/<slug:aslug>', views.view_actor, name='view_actor'),
    path('view_director/<slug:dslug>', views.view_director, name='view_director'),
    path('view_writer/<slug:wslug>', views.view_writer, name='view_writer'),
    path('view_cinematographer/<slug:cslug>', views.view_cinematographer, name='view_cinematographer'),

]
