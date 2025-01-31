from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('update/<int:pk>/', views.update_inventory, name='update_inventory'),
]
