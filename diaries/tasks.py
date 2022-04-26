from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task, Celery

from diaries.models import Diary

app = Celery('diaries')
app.config_from_object('django.conf:settings')


@shared_task(name="check_work_celery")
def print_time():
    delta_time = datetime.datetime.today() - datetime.timedelta(days=10)
    old_diaries = Diary.objects.filter(expiration__lt=delta_time, kind='private')
    old_diaries.delete()
