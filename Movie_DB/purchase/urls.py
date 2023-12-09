from django.contrib import admin
from django.urls import path,include
from purchase import views
app_name='purchase'
urlpatterns = [
    path('',views.booking,name='book ticket'),
]
