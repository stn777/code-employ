import os
from django.db import transaction
from celery import Celery, Task


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_employ.settings')

app = Celery('code_employ')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


class TransactionTask(Task):
    abstract = True

    def apply_async(self, *args, **kwargs):
        transaction.on_commit(
            lambda: super(TransactionTask, self).apply_async(
                *args, **kwargs
            )
        )