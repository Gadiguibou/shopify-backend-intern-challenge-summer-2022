from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),
    path("item/<int:item_id>/edit/", views.item_edit, name="item_edit"),
    path(
        "item/<int:item_id>/edit/submit/", views.item_edit_form, name="item_edit_form"
    ),
    path("item/<int:item_id>/delete/", views.item_delete, name="item_delete"),
    path(
        "item/<int:item_id>/delete/submit/",
        views.item_delete_form,
        name="item_delete_form",
    ),
    path("item/delete-success/<str:item_name>", views.item_delete_success, name="item_delete_success"),
]
