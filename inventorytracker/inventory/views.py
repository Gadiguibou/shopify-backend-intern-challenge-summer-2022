from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from inventory.models import InventoryItem


def index(request):
    all_items = InventoryItem.objects.all().order_by("name")
    return render(request, "inventory/items.html", {"items": all_items})

