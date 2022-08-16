from django_mistune.conf import settings


def get_style(style_name):
    style = settings.MISTUNE_STYLES.get(style_name)
    if style is None:
        raise ValueError(
            f"Unknown style {style_name}. "
            f"Avalaible styles: {', '.join(settings.MISTUNE_STYLES)}"
        )
    return style
