from pytest import raises
from pytest_django.asserts import assertHTMLEqual

from django_mistune.conf import settings
from django_mistune.templatetags.mistune import markdown
from django_mistune.utils import get_style


def test_read_settings():
    assert "custom" in settings.MISTUNE_STYLES
    assert "default" in settings.MISTUNE_STYLES


def test_get_style_unknown():
    with raises(ValueError):
        get_style("unknown")


def test_get_style():
    assert not get_style("custom")["escape"]


def test_simple_gen():
    assertHTMLEqual(
        markdown("**Hello** *World*"),
        "<p><strong>Hello</strong> <em>World</em></p>",
    )


def test_html_escape():
    escaped = "<p>&lt;br&gt;</p>"
    assertHTMLEqual(markdown("<br>"), escaped)
    assertHTMLEqual(markdown("<br>", style_name="custom"), escaped)
