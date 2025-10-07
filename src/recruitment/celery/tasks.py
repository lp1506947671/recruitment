"""
windows启动
celery -A recruitment.interview.tasks worker --loglevel=info -P gevent
"""

from celery import Celery

password = None
# 第一个参数 是当前脚本的名称，第二个参数 是 broker 服务地址
app = Celery(
    "tasks",
    backend=f"redis://:{password}@192.168.190.2",
    broker=f"redis://:{password}@192.168.190.2",
)


@app.task
def add(x, y):
    return x + y
