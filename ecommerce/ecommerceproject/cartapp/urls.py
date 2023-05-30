from . import views
from django.urls import path

app_name='cartapp'
urlpatterns = [
    path('add/<int:prod_id>/',views.add_cart,name='add_cart'),
    path('',views.cartdetails,name='cartdetails'),
    path('delete/<int:prod_id>/',views.cartdelete,name='cartdelete'),
    path('remove/<int:prod_id>/',views.cartremove,name='cartremove'),
]