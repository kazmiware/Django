from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.views.generic import (ListView, DeleteView,View)
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import ecommerce.settings
from .models import Cart
from item.models import Item
from.forms import Order_form


# Create your views here.


def add_item(request, id):

    item = get_object_or_404(Item, id=id)
    print(Cart.objects.filter(item=item))
    if Cart.objects.filter(item=item):
        cart = get_object_or_404(Cart, item=item)
        cart.quantity += 1
        cart.save()
    else:
        cart = Cart.objects.create(item=item)
        item = cart.item
        quantity = cart.quantity
        user_cart = Cart(item=item, quantity=quantity)
        user_cart.save()
        request.user.cart.add(user_cart)

    return render(request, "cart_templates/add_item.html", {})


class CartListView(View):

    template_name = "cart_templates/cart_list.html"
    queryset = Cart.objects.all()

    def get(self, request):

        total = 0
        counter = 0
        for cart_item in request.user.cart.all():
            total += cart_item.quantity*cart_item.item.price

        order_form = Order_form(request.POST or None)
        if order_form.is_valid():
            name = order_form.cleaned_data('name')
            email = order_form.cleaned_data('email')
            address = order_form.cleaned_data('address')
            context = {
                  'name': name,
                  'email': email,
                  'address': address
            }
            html = render_to_string('send_order', context=context)
            send_mail(subject="Order Form Submission",
                      message="Order",
                      from_email="email",
                      recipient_list=[ecommerce.settings.RECIPIENTS_ADDRESS],
                      html_message=html)
            order_form = Order_form()
        return render(request, "cart_templates/cart_list.html", {'form': order_form,
                                                                 'total': total,
                                                                 'count': counter})


class CartDeleteView(DeleteView):
    template_name = "cart_templates/cart_delete.html"
    queryset = Cart.objects.all()
    success_url = "/"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Cart, id=id)




