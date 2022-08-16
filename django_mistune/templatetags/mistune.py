import mistune
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from django_mistune.utils import get_style

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def markdown(text, style_name="default", autoescape=True):
    """Converts `text` to HTML. If a `style_name` is given, it will be loaded
    from the settings.

    The `escape` parameter of the style will always be ignored as it will be
    overriden by the `autoescape` behavior of Django."""
    style = get_style(style_name)
    markdown = mistune.create_markdown(**{**style, "escape": autoescape})

    return mark_safe(markdown(text))
