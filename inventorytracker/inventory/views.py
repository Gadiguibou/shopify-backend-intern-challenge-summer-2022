from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from inventory.models import InventoryItem

import csv
import io


def index(request):
    all_items = InventoryItem.objects.all().order_by("name")
    return render(request, "inventory/items.html", {"items": all_items})


def csv_item_list(request):
    all_items = InventoryItem.objects.all().order_by("name")

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="inventory.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["Name", "Description", "Quantity"])
    for item in all_items:
        writer.writerow([item.name, item.description, str(item.quantity)])

    return response


def item_detail(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    return render(request, "inventory/item_detail.html", {"item": item})


def item_edit(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    return render(request, "inventory/item_edit.html", {"item": item})


def item_edit_form(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)

    try:
        name = request.POST["name"]
        description = request.POST["description"]
        quantity = request.POST["quantity"]
        error_message = _validate_item_form(name, quantity, description)
        if error_message is not None:
            return render(
                request,
                "inventory/item_create.html",
                {"error": error_message},
            )
        else:
            item.name = name
            item.description = description
            item.quantity = quantity
    except KeyError:
        return render(
            request,
            "inventory/item_edit.html",
            {"item": item, "error": "Please fill in all the required fields."},
        )

    item.save()
    return HttpResponseRedirect(reverse("item_detail", args=(item.id,)))


def item_delete(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    return render(request, "inventory/item_delete.html", {"item": item})


def item_delete_form(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    item_name = item.name
    item.delete()
    return HttpResponseRedirect(reverse("item_delete_success", args=(item_name,)))


def item_delete_success(request, item_name):
    return render(
        request, "inventory/item_delete_success.html", {"item_name": item_name}
    )


def item_create(request):
    return render(request, "inventory/item_create.html")


def item_create_form(request):
    try:
        name = request.POST["name"]
        quantity = request.POST["quantity"]
        description = request.POST["description"]
    except KeyError:
        return render(
            request,
            "inventory/item_create.html",
            {"error": "Please fill in all the required fields."},
        )

    print("passed without key errors")

    error_message = _validate_item_form(name, quantity, description)
    if error_message is not None:
        return render(
            request,
            "inventory/item_create.html",
            {"error": error_message},
        )

    item = InventoryItem(name=name, quantity=quantity, description=description)
    item.save()

    return HttpResponseRedirect(reverse("item_detail", args=(item.id,)))


def _validate_item_form(name, quantity, description):
    error_message = ""

    if name is None or quantity is None or description is None:
        error_message += "Please fill in all the required fields."
    if len(name) == 0 or len(name) > 100:
        error_message += "Please fill in the name field."
    if int(quantity) < 0:
        error_message += "Please enter a positive number for the quantity."

    return error_message if len(error_message) > 0 else None
