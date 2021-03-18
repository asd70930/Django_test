from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    products = models.Product.objects.all()
    return render(request, 'phone/index.html', locals())

def detail(request, id):
    try:
        product = models.Product.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    return render(request, 'phone/detail.html', locals())
