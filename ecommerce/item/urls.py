from django.contrib import admin
from django.urls import path
from .views import (ItemListView, ItemDetailView)

app_name = 'item'

urlpatterns = [
    path('', ItemListView.as_view(), name="item_list"),
    path("detail/<int:id>", ItemDetailView.as_view(), name="item_detail"),
    path('shoes/', ItemListView.as_view(template_name='categories/shoes.html'), name="shoes_list"),
    path('watches/', ItemListView.as_view(template_name='categories/watch.html'), name="watch_list"),
    path('shirts/', ItemListView.as_view(template_name='categories/shirt.html'), name="shirt_list"),
    path('jewellery/', ItemListView.as_view(template_name='categories/jewellery.html'), name="jewellery_list")
]
