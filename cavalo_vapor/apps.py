from django.apps import AppConfig


class CavaloVaporConfig(AppConfig):
    name = 'cavalo_vapor'

    def ready(self):
        import cavalo_vapor.signals
