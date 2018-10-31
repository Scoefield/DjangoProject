from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def home(request):
    # 所有商品类别
    alltypes = models.ShopList.objects.all()
    # 类型与商品
    type_and_goods = []
    for typer in alltypes:
        type_and_goods.append((typer, models.ProdList.objects.filter(typer=typer, havup=True)))
    content = {'type_and_goods': type_and_goods, 'alltypes': alltypes}
    return render(request, 'shopping/home.html', content)


def single_web(request, phone_id):
    alltypes = models.ShopList.objects.all()
    # 所属类别
    blg_cgy = get_object_or_404(models.ShopList, id=phone_id)
    # 类型与商品
    type_and_goods = [(blg_cgy, models.ProdList.objects.filter(typer=blg_cgy, havup=True))]
    content = {'type_and_goods': type_and_goods, 'alltypes': alltypes}
    return render(request, 'shopping/home.html', content)


def good_detail(request, phone_id, good_id):
    # 根据商品ID获取商品详细信息
    gd_detail = get_object_or_404(models.ProdList, id=good_id)
    content = {'gd_detail': gd_detail}
    return render(request, 'shopping/detail.html', content)

