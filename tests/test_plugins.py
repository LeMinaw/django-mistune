from pytest_django.asserts import assertHTMLEqual

from django_mistune.templatetags.mistune import markdown


def test_header_level():
    assertHTMLEqual(markdown("# Test", "headers"), "<h3>Test</h3>")


def test_header_level_nested():
    assertHTMLEqual(
        markdown("- Hello\n\n - World\n\n - ## Heading", "headers"),
        """<ul>
            <li><p>Hello</p></li>
            <li><p>World</p></li>
            <li><h4>Heading</h4></li>
        </ul>""",
    )


def test_classes():
    assertHTMLEqual(
        markdown("Hello *World*", "classes"),
        '<p class="a b">Hello <em class="c">World</em></p>',
    )
