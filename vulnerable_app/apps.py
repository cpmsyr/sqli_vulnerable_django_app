from django.apps import AppConfig


class VulnerableAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vulnerable_app'
