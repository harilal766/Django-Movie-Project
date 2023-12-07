from django.urls import path,include
from payment import views

app_name='payment'
urlpatterns = [
    path('add_booking',views.add_booking,name='add_booking'),
]
