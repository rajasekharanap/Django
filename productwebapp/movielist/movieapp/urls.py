from django.contrib import admin
from django.urls import path, include
from . import views

app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:mov>/',views.mid,name='movielist'),
    path('upload/',views.upload,name='upload'),
    path('update/<int:objid>/',views.update,name='update'),
    path('delete/<int:delid>/',views.delete,name='delete'),

]