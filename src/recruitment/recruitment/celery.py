"""
DJANGO_SETTINGS_MODULE=settings.local celery --app recruitment worker -l info -P gevent
celery -A recruitment.interview.tasks worker --loglevel=info -P gevent
"""

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

app = Celery("recruitment")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
