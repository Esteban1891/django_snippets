from django import forms
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("name", "description", "snippet", "language", "public")

    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({'placeholder' : 'nombre del snippet', 'type' : 'text'})
        self.fields["description"].widget.attrs.update({'placeholder' : 'Descripción', 'type' : 'text'})