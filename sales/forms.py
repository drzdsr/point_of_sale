from django import forms
from point_of_sale.models import Sale, SaleDetail

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['user_id', 'customer', 'status', 'payment_method', 'bank_name', 'total_amount', 'discount_percentage']

class SaleDetailForm(forms.ModelForm):
    class Meta:
        model = SaleDetail
        fields = ['product', 'quantity', 'unit_price']
