from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(LoginRequiredMixin, ListView):
    template_name = "snacks/snack_list.html"
    model = Snack
    context_object_name = "snacks"


class SnackDetailView(LoginRequiredMixin, DetailView):
    template_name = "snacks/snack_detail.html"
    model = Snack


class SnackUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "snacks/snack_update.html"
    model = Snack
    fields = "__all__"


class SnackCreateView(LoginRequiredMixin, CreateView):
    template_name = "snacks/snack_create.html"
    model = Snack
    fields = ["name", "fave", "purchaser"] # "__all__" for all of them


class SnackDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "snacks/snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
