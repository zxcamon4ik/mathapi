from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auth_field = "django.db.models.BigAutoField"
    name = "apps.mathFX"
