from . import views
from django.urls import path

app_name='ecommerceapp'
urlpatterns = [
    path('',views.display_products,name='display_products'),
    path('<slug:c_slug>/',views.display_products,name='display_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.product,name='productdet'),
]