from django.shortcuts import render
from .models import Snippet, Language


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'login.html', {})


class IndexView(ListView):
    model = Snippet
    template_name = "index.html"

    def get_queryset(self):
        qs = Snippet.objects.filter(public=True)
        if self.request.user.is_authenticated:
            user_private = Snippet.objects.filter(public=False,user=self.request.user)
            qs = qs.union(user_private)
        return qs.order_by("-created")




def language(request):
    return render(request, 'index.html', {})


def user_snippets(request):
    return render(request, 'snippets/user_snippets.html', {})


def snippet(request):
    return render(request, 'snippets/snippet.html', {})


def snippet_add(request):
    return render(request, 'snippets/snippet_add.html', {})


def snippet_edit(request):
    return render(request, 'snippets/snippet_add.html', {})


def snippet_delete(request):
    return render(request, 'snippets/user_snippets.html', {})
