from .models import Contact_form
from django import forms


class Contact(forms.Form):

    name = forms.CharField(max_length=10, label='', widget=forms.TextInput(
                                                                  attrs={
                                                                          'placeholder': 'Your Name'
                                                                        }
                                                                 )
                           )
    email = forms.EmailField(max_length=20, label='',widget=forms.TextInput(
                                                                    attrs={
                                                                            'placeholder': 'Your Email'
                                                                          }
                                                                   )
                             )
    subject = forms.CharField(max_length=15, label='', widget=forms.TextInput(
                                                                      attrs={
                                                                              'placeholder': 'Your Subject'
                                                                            }
                                                                    )
                              )
    message = forms.CharField(max_length=150, label='', widget=forms.Textarea(
                                                                      attrs={
                                                                              'placeholder': 'Type Your Message Here',
                                                                              'rows': 10
                                                                             }
                                                                     )
                              )

    class Meta:

        model = Contact_form
        fields = [
              'name',
              'email',
              'subject',
              'message',
        ]
