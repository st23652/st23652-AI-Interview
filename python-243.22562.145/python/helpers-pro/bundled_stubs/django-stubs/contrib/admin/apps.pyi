from django.apps import AppConfig

class SimpleAdminConfig(AppConfig):
    default_site: str

class AdminConfig(SimpleAdminConfig): ...
