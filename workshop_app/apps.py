from __future__ import unicode_literals

from django.apps import AppConfig


class WorkshopAppConfig(AppConfig):
    name = 'workshop_app'

    def ready(self):
        import workshop_app.signals
