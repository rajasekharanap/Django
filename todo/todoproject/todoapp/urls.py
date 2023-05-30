from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.task,name='taskpage'),
    # path('taskdetails/',views.taskdetail,name='taskdetail'),
    path('delete/<int:delid>/',views.delete,name='delete'),
    path('update/<int:updid>/',views.update,name='update'),
    path('lstview/',views.Lstview.as_view(),name='listview'),
    path('detview/<int:pk>/',views.Detailview.as_view(),name='detailview'),
    path('updview/<int:pk>/',views.Updateview.as_view(),name='updateview'),
    path('delview/<int:pk>/',views.Deleteview.as_view(),name='deleteview'),
]