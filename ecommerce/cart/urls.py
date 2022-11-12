from django.contrib import admin
from django.urls import path
from .views import (CartListView, add_item, CartDeleteView)

app_name = 'cart'

urlpatterns = [
    path("add/<int:id>/", add_item, name="add_item"),
    path("list/", CartListView.as_view(), name="cart_list"),
    path("item_delete/<int:id>/", CartDeleteView.as_view(), name="delete_item")
]
