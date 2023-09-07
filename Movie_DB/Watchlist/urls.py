
from django.urls import path
from Watchlist import views
app_name='Watchlist'
urlpatterns = [
    path('view_watchlist',views.view_watchlist,name='view_watchlist'),
    path('add_watchlist/<int:p>',views.add_watchlist,name='add_watchlist'),
    path('delete_watchlist/<int:p>',views.delete_watchlist,name='delete_watchlist')
]
