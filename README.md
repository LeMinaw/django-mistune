# django-mistune

[![PyPI - Version](https://img.shields.io/pypi/v/django-mistune.svg)](https://pypi.org/project/django-mistune)
[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/django-mistune.svg)](https://pypi.org/project/django-mistune)
[![PyPI - Django Versions](https://img.shields.io/pypi/frameworkversions/django/django-mistune.svg)](https://pypi.org/project/django-mistune)
[![Codecov - Coverage](https://img.shields.io/codecov/c/github/LeMinaw/django-mistune.svg)](https://app.codecov.io/github/LeMinaw/django-mistune)


Simple yet customizable Django template filter to render Markdown using the
awesome [Mistune][m_docs] package.

-----

## Installation

Install the package with `pip` or any tool of your choice:

```console
pip install django-mistune
```

Add `django_mistune` to `INSTALLED_APPS` in Django `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_mistune',
    ...
]
```

You're all set!

## How to use

### In a nutshell

In templates, the `markdown` filter will render any Markdown fragment to HTML:

```jinja
{% load mistune %}

...

{{ some_markdown_text|markdown }}
```

Like all other filters, this can also be used in Python code:

```py
from django_mistune.templatetags.mistune import markdown

markdown("**Hello** *World*")
# -> "<p><strong>Hello</strong> <em>World</em></p>"
```

### Using styles

For more advanced uses, the `markdown` filter accepts an optionnal style name
parameter.

```jinja
{{ some_markdown_text|markdown:"fancy" }}
```

Mistune styles can be defined in `settings.py`, and contains arguments to be
passed to [`mistune.create_markdown`][m_create_md]:

```py
MISTUNE_STYLES = {
    # Let's enable the strikethrough plugin by default
    "default": {
        "plugins": ["strikethrough"],
    },
    # Create a `fancy` style where every linebreak is rendered
    "fancy": {
        "hard_wrap": True,
    }
}
```

*__Note:__ The `escape` parameter has no effect, as the current Django escaping
behavior will always be used instead.*

When no style is specified, the `"default"` style will be used.

### More fun with plugins

Mistune supports plugins, and comes with [a large variety of those][m_plugins],
as the `"strikethrough"` plugin of the previous example.

`django-mistune` also comes with a comprehensive sets of plugins, useful when
rendering markdown for the web. You can browse [the plugins module][plugins] of
this repo to see them.

It is also possible to [create your own plugins][m_create_plugins].

Here is a quick showcase of the plugins `django-mistune` has to offer:

```py
from django_mistune.plugins import AddClasses, HeaderLevels, TargetBlankLinks

...

MISTUNE_STYLES = {
    'default': {
        'plugins': [
            HeaderLevels(top=4),  # Demote headings so the top level is H4
            AddClasses({  # Add those classes to all following HTML elements
                'ul': 'browser-default', 
                'img': ('responsive-img', 'materialboxed'),
            }),
            TargetBlankLinks(),  # Add `target="_blank"` to all links
        ]
    },
}
```

## Contributing

### Setup

`django-mistune` needs [Hatch][hatch_install] to be installed for project
management.

Use `hatch env create` to install the project in development mode in a managed
virtual environment.

### Format / lint / autofix

Use `hatch fmt` (you can add the `--check` option to disable autofix).

### Running tests

- `hatch run test:test` Run a single test session
- `hatch run test:cov` Run a single test session and output coverage
- `hatch run matrix:test` Run the test suite against the full test matrix

## License

`django-mistune` is distributed under the terms of the [MIT][mit] license.

[m_docs]: https://mistune.lepture.com/en/v2/
[m_create_md]: https://mistune.lepture.com/en/v2/api.html#mistune.create_markdown
[m_plugins]: https://mistune.lepture.com/en/v2/plugins.html
[plugins]: https://github.com/LeMinaw/django-mistune/blob/master/django_mistune/plugins.py
[m_create_plugins]: https://mistune.lepture.com/en/v2/advanced.html#create-plugins
[hatch_install]: https://hatch.pypa.io/latest/install/
[mit]: https://spdx.org/licenses/MIT.html
