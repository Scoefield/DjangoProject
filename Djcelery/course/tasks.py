# -*- coding:utf-8 -*-
# --------------------------
# Author: dys
# Datetime: 18-11-3 下午3:41
# Filename: tasks.py
# --------------------------
from celery.task import Task
import time
from django.http import JsonResponse


class CourseTask(Task):
    name = 'course-task'    # 设置任务的名字

    def run(self, *args, **kwargs):
        print("Start course task...")
        time.sleep(8)
        print("args={}, kwargs={}".format(args, kwargs))
        print("End course task...")
        result = {'worker_result': 'ok done'}
        return JsonResponse(result)

