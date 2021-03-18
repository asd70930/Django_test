# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin
# Create your models here.


class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')  # 一張資料正在處理中的圖片

    def __str__(self):
        return self.name


class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default='超值二手機', verbose_name='型號')
    description = models.TextField(default='暫無說明', verbose_name='摘要')
    year = models.IntegerField(default=2016, verbose_name='出廠年份')
    price = models.IntegerField(default=0, verbose_name='價格')

    def __str__(self):
        return self.nickname


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    search_fields = ('nickname',)
    ordering = ('-price',)

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='產品圖片')
    url = models.URLField(default='http://i.imgur.com/Z230eeq.png')

    def __str__(self):
        return self.description





