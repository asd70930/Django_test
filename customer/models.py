from django.db import models
from django.contrib import admin
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    stock_pcs = models.IntegerField()
    price = models.IntegerField()
    shop_id = models.CharField(max_length=100)
    vip = models.BooleanField()



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 名稱不可更改成別的，否則Django無法辨識
    # list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']
    # 同等上面的
    list_display = [field.name for field in Product._meta.fields]

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    qty = models.IntegerField()
    customer_id = models.CharField(max_length=100)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # 名稱不可更改成別的，否則Django無法辨識
    list_display = [field.name for field in Order._meta.fields]