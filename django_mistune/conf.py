from types import SimpleNamespace

from django.conf import settings as dj_settings

settings = SimpleNamespace(
    # A style is basically a dict containing parameters to pass to `mistune`
    MISTUNE_STYLES={
        **{
            "default": {
                # The `escape` parameter is useless as it will be overriden
                # according to Django `autoescape`
                "hard_wrap": False,
                "renderer": "html",
                "plugins": [],
            },
        },
        **getattr(dj_settings, "MISTUNE_STYLES", {}),
    }
)
