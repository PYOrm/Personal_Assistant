from django.db.models.signals import post_migrate
from django.dispatch import receiver
from background_task.models import Task
from latest_news.utils.updater import run_parsers
from datetime import datetime 

@receiver(post_migrate)
def schedule_update_task(sender, **kwargs):
    if not Task.objects.filter(task_name='latest_news.utils.updater.run_parsers').exists():
        run_parsers(schedule=datetime.now())  
        run_parsers(repeat=3600)  
