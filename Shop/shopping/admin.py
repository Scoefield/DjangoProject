from django.contrib import admin
from . import models

# Register your models here.


class ShopListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']


admin.site.register(models.ShopList, ShopListAdmin)
# admin.site.register(models.ShopList)


class ProdListAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'price', 'typer', 'having', 'havup', 'creatime', 'moditime']
    list_editable = ['price', 'typer', 'having', 'havup']
    list_per_page = 6


admin.site.register(models.ProdList, ProdListAdmin)
