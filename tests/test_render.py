from django.template import Context, Template
from pytest import fixture
from pytest_django.asserts import assertHTMLEqual


def assert_renders(template, result, **kwargs):
    """Small utility function to render Django templates quickly."""
    assertHTMLEqual(template.render(Context(kwargs)), result)


@fixture
def default_template():
    return Template(
        r"""{% load mistune %}
        {{ text|markdown }}"""
    )


@fixture
def noescape_template():
    return Template(
        r"""{% load mistune %}
        {% autoescape off %}
        {{ text|markdown }}
        {% endautoescape %}"""
    )


def test_simple_render(default_template):
    assert_renders(
        default_template,
        "<p><strong>Hello</strong> <em>World</em></p>",
        text="**Hello** *World*",
    )


def test_escape(default_template):
    assert_renders(default_template, "<p>&lt;br&gt;</p>", text="<br>")


def test_noescape(noescape_template):
    assert_renders(noescape_template, "<br>", text="<br>")
