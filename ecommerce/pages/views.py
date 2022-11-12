from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from ecommerce.settings import RECIPIENTS_ADDRESS
from .forms import Contact

# Create your views here.


def contact_view(request):

    form = Contact(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data('name')
        email = form.cleaned_data('email')
        subject = form.cleaned_data('subject')
        message = form.cleaned_data('message')
        context = {
              'name': name,
              'email': email,
              'subject': subject,
              'message': message
        }
        html = render_to_string("contact/send_contact.html", context)
        send_mail(subject="Your subject",
                  message="Your message",
                  from_email="Your email",
                  recipient_list=[RECIPIENTS_ADDRESS],
                  html_message=html)
        form = Contact()

    return render(request, "pages/contact_us.html", {'form': form})



