"""
URL configuration for point_of_sale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# pos_system/urls.py

from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),  # Set the dashboard view as the root URL
    path('products/', include('products.urls')),
    path('sales/', include('sales.urls')),
    path('customers/', include('customers.urls')),
    path('inventory/', include('inventory.urls')),
    path('reports/', include('reports.urls')),
]


