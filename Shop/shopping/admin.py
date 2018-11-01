from django.contrib import admin
from . import models

# Register your models here.


class ShopListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']      # 在后台管理显示相应字段数据


admin.site.register(models.ShopList, ShopListAdmin)
# admin.site.register(models.ShopList)


class ProdListAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'price', 'typer', 'having', 'havup', 'creatime', 'moditime']
    list_editable = ['price', 'typer', 'having', 'havup']   # 可编辑的字段
    list_per_page = 6       # 每页显示6条数据


admin.site.register(models.ProdList, ProdListAdmin)
