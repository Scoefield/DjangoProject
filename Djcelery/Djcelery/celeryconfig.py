# -*- coding:utf-8 -*-
# --------------------------
# Author: dys
# Datetime: 18-11-3 下午3:41
# Filename: celeryconfig.py
# --------------------------
import djcelery
from datetime import timedelta

djcelery.setup_loader()

# 设置队列名称
CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_queue': {
            'exchange': 'work_queue',
            'exchange_type': 'direct',
            'binding_key': 'work_queue'
        },
}

# 默认队列
CELERY_DEFAULT_QUEUE = 'work_queue'

# 导入任务（tasks.py）
CELERY_IMPORTS = (
    'course.tasks',
)

# 非常重要，有些情况下防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的worker数量
CELERYD_CONCURRENCY = 4

# 失败后允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务就会被销毁被销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间，否则会被SIGKILL信号杀死
CELERYD_TASKS_TIME_LIMIT = 12 * 30


# 设置定时调度的任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'course-task',  # 调度的任务名称
        'schedule': timedelta(seconds=5),    # 每5秒调度一次
        'options': {
            'queue': 'beat_tasks',  # 选择队列名称
        }
    }
}
