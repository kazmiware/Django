from django import forms
from.models import Order


class Order_form(forms.Form):

    name = forms.CharField(max_length=10, label='', widget=forms.TextInput(
                                                                attrs={
                                                                       'placeholder': 'Your Name'
                                                                      }
                                                                          )
                           )
    email = forms.EmailField(max_length=20, label='', widget=forms.TextInput(
                                                            attrs={
                                                                    'placeholder': 'Your Email'
                                                                  }
                            )
                                                                             )
    address = forms.CharField(max_length=15, label='', widget=forms.TextInput(
                                                                attrs={
                                                                       'placeholder': 'Your Address'
                                                                        }
                                                                              )
                              )

    class Meta:

        model = Order
        fields = [
            "name",
            "email",
            "address",
        ]
