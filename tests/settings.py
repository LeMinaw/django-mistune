from django_mistune.plugins import AddClasses, HeaderLevels, TargetBlankLinks

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
    "noescape": {"escape": False},
    "headers": {"plugins": [HeaderLevels(3)]},
    "classes": {"plugins": [AddClasses({"p": ("a", "b"), "em": "c"})]},
    "links": {"plugins": [TargetBlankLinks()]},
}
