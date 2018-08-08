from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from ..css import transform_css_urls
from ..loader import load_staticfile


register = template.Library()


@register.simple_tag
def inline_staticfile(name):
    return load_staticfile(name, fail_silently=not settings.DEBUG)


@register.simple_tag
def inline_style(name):
    return mark_safe(load_staticfile(
        name, transform_css_urls, fail_silently=not settings.DEBUG))


@register.simple_tag
def inline_javascript(name):
    return mark_safe(load_staticfile(name, fail_silently=not settings.DEBUG))
