from django.apps import AppConfig


class LatestNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'latest_news'

    def ready(self):
        # Import signal handlers
        import latest_news.signals
