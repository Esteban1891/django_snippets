from __future__ import unicode_literals

from django.db import models
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter



class Language(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

def set_language_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return
    uuid_slug = str(uuid.uuid4())[:6]
    instance.slug = slugify("{}-{}".format(instance.name,uuid_slug))

pre_save.connect(set_language_slug, sender=Language)


class Snippet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    snippet = models.TextField(blank=False, null=False)
    language = models.ForeignKey(Language,on_delete=models.CASCADE, blank=False, null=False)
    public = models.BooleanField(default=False)

    def pigmented_snippet(self):
        lexer = get_lexer_by_name(self.language.name, stripall=True)
        formatter = HtmlFormatter(linenos=True, cssclass="source")
        result = highlight(self.snippet, lexer, formatter)
        return result

    class Meta:
        ordering = ("-created",)
