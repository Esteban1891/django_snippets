from django.http import request
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snippet, Language
from django.urls import reverse_lazy
from .forms import SnippetForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import get_user_model


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


class SnippetUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Snippet
    template_name = "snippets/snippet_add.html"
    form_class = SnippetForm

    def test_func(self):
        snip=self.get_object()
        return self.request.user==snip.user

    def get_success_url(self):
        return reverse_lazy('snippet',kwargs={"pk":self.object.pk})    


class SnippetDeleteView(UserPassesTestMixin,DeleteView):
    model = Snippet
    template_name = 'snippets/snippet_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        snip=self.get_object()
        return self.request.user==snip.user


class SnippetLanguageListView(ListView):
    model = Snippet
    template_name = "snippets/language.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["language"] = get_object_or_404(Language, slug=self.kwargs['lang']).name
        return context

    def get_queryset(self):
        self.lang = get_object_or_404(Language, slug=self.kwargs['lang'])
        qs = Snippet.objects.filter(public=True, language=self.lang)
        if self.request.user.is_authenticated:
            user_private = Snippet.objects.filter(public=False,user=self.request.user, language=self.lang)
            qs = qs.union(user_private)
        return qs.order_by("-created")


class SnippetUserListView(ListView):
    model = Snippet
    template_name = "snippets/user_snippets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creator"] = self.kwargs["username"]
        return context

    def get_queryset(self):
        self.creator = get_object_or_404(get_user_model(), username=self.kwargs['username'])
        print(self.creator)
        qs = Snippet.objects.filter(public=True, user=self.creator)
        if self.request.user.is_authenticated and self.request.user == self.creator:
            user_private = Snippet.objects.filter(public=False,user=self.request.user)
            qs = qs.union(user_private)
        return qs.order_by("-created")