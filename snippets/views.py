from django.shortcuts import render
from .models import Snippet, Language
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


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

