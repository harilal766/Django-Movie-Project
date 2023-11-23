from django.urls import path
from Search import views
app_name='Search'
urlpatterns = [
    path('search_movie',views.searchmovie,name='search_movie'),
    path('advanced_search',views.advanced_search,name='advanced_search'),
]