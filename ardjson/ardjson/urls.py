from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('objconn/', views.objconnView, name='objconn'),    
    path('sound/', views.soundView, name='sound'),
    path('photoresistance/', views.photoresistanceView, name='photoresistance'),    
    path('dht11/', views.dht11View, name='dht11'),
    path('master/', views.masterView, name='master'),
    path('room101/', views.room101View, name='room101'),
    path('room102/', views.room102View, name='room102'),
    path('room103/', views.room103View, name='room103'),
    path('add_obj/', views.add_objView, name='add_obj'),
    path('api/save-data/', views.savedataView, name='save_data'),
    path('delete_obj/<int:obj_id>/', views.delete_obj_view, name='delete_obj'),
    path('upd_obj/<int:obj_id>/', views.upd_obj_view, name='upd_obj'),
]

