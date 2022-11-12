from django.shortcuts import get_object_or_404, render
from django.views.generic import (ListView, DetailView)
from django.contrib.auth.forms import UserCreationForm
from.models import Item

# Create your views here.


class ItemListView(ListView):

    template_name = "item_templates/item_list.html"
    queryset = Item.objects.all()


class ItemDetailView(DetailView):

    template_name = "item_templates/item_detail.html"
    queryset = Item.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Item, id=id)


def signup_view(request):

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserCreationForm(request.post or None)
    return render(request, "registration/sign_up.html", {"form": form})





