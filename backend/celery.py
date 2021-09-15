from __future__ import absolute_import, unicode_literals

import os

import celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

import configurations

configurations.setup()

app = celery.Celery('backend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'scrap-yt-every-10-seconds': {
        'task': 'backend.worker.tasks.yt_scrapper_task',
        'schedule': 10.0,
    },
}
app.conf.timezone = 'UTC'