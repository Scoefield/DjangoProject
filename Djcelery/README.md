# Django之celery应用
## Celery是什么？
1. 简单、灵活且可靠的，处理消息的分布式系统
2. 专注于实时处理异步任务队列
3. 也支持任务调度

## Celery使用场景：
1. 异步处理：将耗时操纵提交给Celery去异步执行，比如短信、消息推送和音频处理等
2. 定时任务：类似crontab，比如每日数据统计

## 在Django应用celery的简单步骤如下：
1. 创建Django项目：django-admin startproject Djcelery
2. 创建app：django-admin startapp course 或 python manage.py startapp course
3. pip install django-celery
4. 将app和djcelery注册到settings.py里，并将redis相关设置写到settings.py里
5. 在工程Djcelery下（跟settings.py同级目录）new一个celeryconfig.py，并将相应的配置内容写进去
6. 在App目录下（跟view.py同级目录）new一个tasks.py，在里面编写任务类和任务名称
7. urls.py里配置相应的路由，并编辑view.py(将路由对应的函数在view里实现)
8. 测试Django和celery
    * 开启Django服务：python manage.py runserver，也可运行run_web.sh，然后在浏览器地址栏输入：http://127.0.0.1:8000/do
    * 开启worker：python manage.py celery worker -l INFO（领取并执行redis待处理的任务）
    * 定时调度任务：python manage.py celery beat -l INFO（在redis队列增加任务）
    * 注意：可运行run_celery_worker.sh和run_celery_beat.sh脚本执行命令

## 监控工具Flower如下：
1. Install: pip install flower
2. Start: celery flower --address=0.0.0.0 --port=5555 --broker=xxxx --basic_auth=user:passwd
    * eg1: python manage.py celery flower (先启动worker后，再启动flower)
    * eg2: python manage.py celery flower --basic_auth=admin:admin123 (其中basic_auth为要设置的验证账号和密码，用于在web端验证)，启动后可在浏览器地址栏输入：http://127.0.0.1:5555，然后在web可对celery进行监控
    * 注意：可运行run_flower.sh脚本执行命令

## 进程管理工具supervisor如下：
1. Install: pip install supervisor
    * 注意：supervisor的安装python2才支持用pip安装，python3用sudo apt-get install supervisor安装
2. 在工程Djcelery下（跟App同级目录）new一个conf文件夹，然后生成配置文件：echo_supervisord_conf > conf/supervisord.conf
3. 编辑supervisord.conf文件：一般是打开[supervisorctl]下的serverurl、[inet_http_server]下的port和[include]下的files的注释(files=*.ini)
4. 在conf目录下根据需要分别新建supervisor_celeery_worker.ini、supervisor_celery_beat.ini、supervisor_celery_flower.ini文件，然后根据supervisor官网<http://supervisord.org/>的文档说明对这些ini文件进行编辑
5. 启动supervisord: supervisord -c conf/supervisord.conf
    * 若没有报错，则可以在终端输入：ps -aux | grep supervisor (linux下)查看supervisor进程，如果是Mac下，则把-aux改为-ef即可
    * 然后在浏览器输入：http://127.0.0.1:9001 查看进程状况
