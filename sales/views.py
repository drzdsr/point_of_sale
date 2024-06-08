from django.shortcuts import render, redirect
from point_of_sale.models import *
from django.contrib import messages



from django.shortcuts import render, redirect
from .forms import SaleForm, SaleDetailForm
from products.forms import ProductForm

def create_sale(request):
    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        if sale_form.is_valid():
            sale = sale_form.save()
            # Additional logic to handle adding products to sale can be implemented here
            return redirect('sale_detail', sale_id=sale.sale_id)
    else:
        sale_form = SaleForm()
    return render(request, 'create_sale.html', {'sale_form': sale_form})

def sale_detail(request, sale_id):
    sale = Sale.objects.get(pk=sale_id)
    sale_details = SaleDetail.objects.filter(sale=sale)
    return render(request, 'sale_detail.html', {'sale': sale, 'sale_details': sale_details})


def delete_sale(request, sale_id):
    sale = Sale.objects.get(pk=sale_id)
    sale.delete()
    return redirect('sale_list')

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale_list.html', {'sales': sales})


def add_new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('add_new_product')  # Redirect to clear the form
    else:
        form = ProductForm()

    context = {
        'form': form,
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
        'barcodes': Barcode.objects.all()
    }

    return render(request, 'add_new_product.html', context)