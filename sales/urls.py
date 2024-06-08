from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_sale, name='create_sale'),
    path('<int:sale_id>/', views.sale_detail, name='sale_detail'),
    path('<int:sale_id>/delete/', views.delete_sale, name='delete_sale'),
    path('sale_list', views.sale_list, name='sale_list'),
    path('add_new_product/', views.add_new_product, name='add_new_product'),

]
