"""
# celery定时任务调度器
celery -A recruitment beat --scheduler django_celery_beat.schedulers:DatabaseScheduler

# 启动celery任务队列
celery -A recruitment  worker --loglevel=info -P gevent
DJANGO_SETTINGS_MODULE=settings.local celery --app recruitment worker -l info -P gevent

# flower 监控任务队列
 celery -A recruitment  flower --broker=redis://192.168.190.:6379/0

"""

import json
import os

from celery import Celery
from celery.schedules import crontab
from django_celery_beat.models import IntervalSchedule, PeriodicTask

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

app = Celery("recruitment")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.timezone = "Asia/Shanghai"  # 设置一下 celery 时区


@app.task
def test(arg):
    print(arg)


# 方式一:直接配置定时任务
app.conf.beat_schedule = {
    "add-every-10-seconds": {
        "task": "recruitment.tasks.add",
        "schedule": 10.0,
        "args": (
            16,
            4,
        ),
    },
}


def dynamic_create_task(name, task, args, schedule):
    # 1.创建定时策略
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10, period=IntervalSchedule.SECONDS
    )
    # 2.创建任务
    PeriodicTask.objects.create(
        interval=schedule,
        name="say welcome1",
        task="recruitment.celery.test",
        args=json.dumps(["welcome"]),
    )


# 方式二:在系统启动时注册定时任务
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s("hello"), name="hello every 10")

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s("world"), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1), test.s("Happy Mondays!")
    )
