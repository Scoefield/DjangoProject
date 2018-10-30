from django.db import models


# Create your models here.
class ShopList(models.Model):
    name = models.CharField(max_length=50, unique=True)
    disc = models.TextField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='category', blank=True)

    class Meta:
        # 这个选项是指定，模型的复数形式是什么，比如：verbose_name_plural = "stories"
        verbose_name_plural = "ShopList"
        # 指定表名
        db_table = "ShopList"

    def __str__(self):
        return self.name


class ProdList(models.Model):
    name = models.CharField(max_length=50, unique=True)
    disc = models.TextField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='category', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # 所属类型，跟随ShopList表更改
    typer = models.ForeignKey(ShopList, on_delete=models.CASCADE)
    having = models.IntegerField(default=0)
    havup = models.BooleanField(default=True)
    creatime = models.DateTimeField(auto_now_add=True)
    moditime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ProdList"
        db_table = "ProdList"

    def __str__(self):
        return self.name
