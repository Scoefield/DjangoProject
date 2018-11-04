from django.shortcuts import render
from course.tasks import CourseTask
from django.http import JsonResponse


# Create your views here.
def do(request):
    print("Start do request...")
    # CourseTask.delay()  # delay执行队列，没有填写指定队列的话，会默认执行配置文件设置默认的队列
    CourseTask.apply_async(args=('hello',), queue='work_queue')  # 传入参数，并指定work_queue队列
    print("End do request...")
    result = {'result': 'waiting...'}
    return JsonResponse(result)

