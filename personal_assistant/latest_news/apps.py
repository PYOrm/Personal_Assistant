from django.apps import AppConfig


class LatestNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'latest_news'

    def ready(self):
        from latest_news.utils import updater
        updater.start()
