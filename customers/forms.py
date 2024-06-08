from django import forms
from point_of_sale.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
