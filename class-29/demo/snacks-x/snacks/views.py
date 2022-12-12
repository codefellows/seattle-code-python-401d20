from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
    template_name = "snacks/snack-list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "snacks/snack-detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snacks/snack-create.html"
    model = Snack
    fields = ['name','description','purchaser']


class SnackUpdateView(UpdateView):
    template_name = "snacks/snack-update.html"
    model = Snack
    fields = ['name','description']


class SnackDeleteView(DeleteView):
    template_name = "snacks/snack-delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
