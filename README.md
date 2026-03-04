# django-mistune

[![PyPI - Version](https://img.shields.io/pypi/v/django-mistune.svg)](https://pypi.org/project/django-mistune)
[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/django-mistune.svg)](https://pypi.org/project/django-mistune)
[![PyPI - Django Versions](https://img.shields.io/pypi/frameworkversions/django/django-mistune.svg)](https://pypi.org/project/django-mistune)

Simple yet customizable Django template filter to render Markdown using the
awesome [Mistune](https://mistune.readthedocs.io/en/latest/) package.

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install django-mistune
```

## Contributing

### Setup

`django-mistune` needs [Hatch](https://hatch.pypa.io/latest/install/) to be
installed for project management.

Use `hatch env create` to install the project in development mode in a managed
virtual environment.

### Format / lint / autofix

Use `hatch fmt` (you can add the `--check` option to disable autofix).

### Running tests

- `hatch run test:test` Run a single test session
- `hatch run test:cov` Run a single test session and output coverage
- `hatch run matrix:test` Run the test suite against the full test matrix

## License

`django-mistune` is distributed under the terms of the
[MIT](https://spdx.org/licenses/MIT.html) license.
