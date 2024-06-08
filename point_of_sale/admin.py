
from django.contrib import admin
from point_of_sale.models import Customer, Category, Brand, Barcode, Product, Inventory, Sale, SaleDetail, SalesReport, StockReport

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Barcode)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.register(SalesReport)
admin.site.register(StockReport)
