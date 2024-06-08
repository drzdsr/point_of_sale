from django.shortcuts import render, get_object_or_404, redirect
from point_of_sale.models import Inventory
from .forms import InventoryForm

def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventories': inventories})

def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'update_inventory.html', {'form': form})
