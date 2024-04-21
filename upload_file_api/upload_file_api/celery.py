import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "upload_file_api.settings")

app = Celery('upload_file_api')
app.config_from_object("django.conf:settings", namespace="CELERY")

# это важно!
app.conf.update(
    BROKER_URL='redis://redis:6379/0',
    CELERY_RESULT_BACKEND='redis://redis:6379/0',
)

app.autodiscover_tasks()
