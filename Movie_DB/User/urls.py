from django.urls import path
from User import views
app_name='User'
urlpatterns = [
    path('edit_user',views.edit_user,name='edit_user'),

    # path('edit_user',views.Update_User.as_view(),name='edit_user'),

    path('userprofile',views.userprofile,name='userprofile'),
]