from django.apps import AppConfig


class SshConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ssh'

    def ready(self):
        from . import receivers
