from django.contrib import admin
from django.urls import path,include
from Movies import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('movies',views.MovieViewSet)
router.register('users',views.UserViewSet)
app_name='Movie'
urlpatterns = [
    # API
    path('api-auth/',include(router.urls)),
    # function based path
    path('',views.home,name='home'),
    path('view_movies',views.view_movies,name='view_movies'),
    path('add_movie',views.add_movie,name='add_movie'),

    # path('delete_movie/<slug:mslug>',views.delete_movie,name='delete_movie'),
    path('delete_movie/<int:pk>',views.Delete_Movie.as_view(),name='delete_movie'),

    path('edit_movie/<slug:mslug>',views.edit_movie,name='edit_movie'),
    # path('edit_movie/<int:pk>',views.Update_Movie.as_view(),name='edit_movie'),

    path('view_movie/<slug:mslug>',views.view_movie,name='view_movie'),

    path('add_review/<slug:mslug>',views.add_review,name='add_review'),
    path('delete_review/<int:pk>',views.Delete_Review.as_view(),name='delete_review'),
    # user
    path('signup',views.register,name='signup'),
    path('signin',views.usersignin,name='signin'),
    path('signout',views.usersignout,name='signout'),
]

# API Authorization
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/',views.obtain_auth_token)
]