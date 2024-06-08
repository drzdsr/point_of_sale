from django.shortcuts import render
from point_of_sale.models import Sale
from point_of_sale.models import Inventory

def sales_report(request):
    sales = Sale.objects.all()
    return render(request, 'sales_report.html', {'sales': sales})

def inventory_report(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory_report.html', {'inventories': inventories})
