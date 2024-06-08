from django import forms
from point_of_sale.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'brand', 'barcode', 'store_keeping_unit', 'product_name', 'description', 'quantity', 'reorder_level', 'cost_price', 'selling_price']
