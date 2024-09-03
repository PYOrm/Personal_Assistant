from django.apps import AppConfig


class LatestNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'latest_news'

    def ready(self):
        if __name__ == "latest_news.apps":
            from latest_news.utils import updater
            updater.start()
