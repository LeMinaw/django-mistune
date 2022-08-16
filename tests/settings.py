USE_TZ = True  # Avoid deprecation warning

INSTALLED_APPS = [
    "django_mistune",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
    },
]

MISTUNE_STYLES = {
    "custom": {"escape": False},
}
