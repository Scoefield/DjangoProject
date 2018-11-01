from django.db import models


# Create your models here.
class ShopList(models.Model):
    name = models.CharField(max_length=50, unique=True)         # 类别名称
    disc = models.TextField(max_length=100, blank=True)         # 类别描述
    photo = models.ImageField(upload_to='category', blank=True) # 类别图片

    class Meta:
        # 这个选项是指定，模型的复数形式是什么，比如：verbose_name_plural = "stories"
        verbose_name_plural = "ShopList"
        # 指定表名
        db_table = "ShopList"

    def __str__(self):      # python3 在管理后台显示数据名称（若没有这个只显示对象），python2为__unicode__(self)
        return self.name


class ProdList(models.Model):
    name = models.CharField(max_length=50, unique=True)             # 商品名称
    disc = models.TextField(max_length=100, blank=True)             # 商品描述
    photo = models.ImageField(upload_to='category', blank=True)     # 商品图片
    price = models.DecimalField(max_digits=10, decimal_places=2)    # 商品价格
    # 所属类型，跟随ShopList表更改
    typer = models.ForeignKey(ShopList, on_delete=models.CASCADE)   # 商品类型
    having = models.IntegerField(default=0)                         # 库存
    havup = models.BooleanField(default=True)                       # 是否上架
    creatime = models.DateTimeField(auto_now_add=True)              # 创建时间
    moditime = models.DateTimeField(auto_now_add=True)              # 修改时间

    class Meta:
        verbose_name_plural = "ProdList"
        ordering = ['creatime']     # 按照创建时间来排序
        db_table = "ProdList"

    def __str__(self):
        return self.name
