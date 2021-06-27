from django.shortcuts import render
from .models import Snippet, Language
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import SnippetForm


class IndexView(ListView):
    model = Snippet
    template_name = "index.html"

    def get_queryset(self):
        qs = Snippet.objects.filter(public=True)
        if self.request.user.is_authenticated:
            user_private = Snippet.objects.filter(public=False,user=self.request.user)
            qs = qs.union(user_private)
        return qs.order_by("-created")

class SnippetDetailView(UserPassesTestMixin,DetailView):
    model = Snippet
    
    def test_func(self):
        snip = self.get_object()
        return snip.public or self.request.user == snip.user



class SnippetCreateView(LoginRequiredMixin,CreateView):
    model = Snippet
    template_name = "snippets/snippet_add.html"
    form_class = SnippetForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('snippet',kwargs={"pk":self.object.pk})
