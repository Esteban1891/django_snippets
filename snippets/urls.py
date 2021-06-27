from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('snippets/snippet/<int:pk>', views.SnippetDetailView.as_view(), name='snippet'),
    path('snippets/add/', views.SnippetCreateView.as_view(), name='snippet_add'),
    path('snippets/edit/<int:pk>', views.SnippetUpdateView.as_view(), name='snippet_edit'),
    path('snippets/delete/<int:pk>', views.SnippetDeleteView.as_view(), name='snippet_delete'),
    path('snippets/lang/<slug:lang>', views.SnippetLanguageListView.as_view(), name='language'),
    path('snippets/user/<str:username>/', views.SnippetUserListView.as_view(), name='user_snippets'),
]