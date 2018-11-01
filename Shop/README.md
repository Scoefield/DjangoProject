# 用Django 2.0 制作简单的购物网站
## 环境搭建：Django2.0 + python3
## Model与后台/自定义后台/Templates、Views 和 Urls/完善主页逻辑/制作详情页

---
* 创建Django工程和App，然后在浏览器输入：<http://127.0.0.1:8000>测试Django
```
django-admin startproject Shop
django-admin startapp shopping
python3 manage.py runserver
```
* 编辑model.py建立相关字段
* 检查和记录对model的改动，将该改动作用到数据库文件，比如产生table，修改字段的类型等。然后创建超级用户
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
* 中间编辑settings.py、urls和views.py等详细步骤请参考网上教程!