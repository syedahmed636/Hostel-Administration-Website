from django.urls import path
from . import views
urlpatterns = [

    path('adminpanel',views.adminpanel,name='adminpanel'),
    path('adduser', views.adduser, name='adduser'),
    path('fetchuser', views.fetchuser, name='fetchuser'),
    path('updateuser/<int:id>', views.updateuser, name='updateuser'),
    path('deleteuser/<int:id>', views.deleteuser, name='deleteuser'),
    path('profile', views.profile, name='profile'),
    path('updateprofile/<int:id>', views.updateprofile, name='updateprofile'),
    path('deleteprofile/<int:id>', views.deleteprofile, name='deleteprofile')

]
