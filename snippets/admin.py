from django.contrib import admin
from django import forms
from .models import Language


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        exclude = ['slug']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    form = LanguageForm