from django import forms
from point_of_sale.models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
