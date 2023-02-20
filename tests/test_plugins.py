from pytest import mark
from pytest_django.asserts import assertHTMLEqual

from django_mistune.templatetags.mistune import markdown

ALL_STYLES = ("style", ("headers", "classes", "links"))


@mark.parametrize(*ALL_STYLES)
def test_empty_string(style):
    assertHTMLEqual(markdown("", style), "")


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


def test_classes_existing_attrs():
    assertHTMLEqual(
        markdown("This ![image](test.jpg)", "classes"),
        '<p class="a b">This <img src="test.jpg" alt="image" class="d"></p>',
    )


def test_classes_multiple_roots():
    assertHTMLEqual(
        markdown("foo\n\nbar", "classes"),
        '<p class="a b">foo</p><p class="a b">bar</p>',
    )


def test_links():
    target = '<p><a target="_blank" href="example.com">Link</a></p>'
    assertHTMLEqual(markdown("[Link](example.com)", "links"), target)
    assertHTMLEqual(markdown("[Link][1]\n\n[1]: example.com", "links"), target)
