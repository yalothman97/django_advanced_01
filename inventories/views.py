from django.shortcuts import render
from .models import Inventory

def inventory_list(request):
    inventory = Inventory.objects.all()
    context = {
        "inventorys": inventory
    }
    return render(request, 'list.html', context)