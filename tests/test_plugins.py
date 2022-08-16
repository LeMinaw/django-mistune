from pytest_django.asserts import assertHTMLEqual

from django_mistune.templatetags.mistune import markdown


def test_header_level():
    assertHTMLEqual(markdown("# Test", "headers"), "<h3>Test</h3>")


def test_classes():
    assertHTMLEqual(
        markdown("Hello *World*", "classes"),
        '<p class="a b">Hello <em class="c">World</em></p>',
    )
