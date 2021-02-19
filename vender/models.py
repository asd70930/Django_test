from django.db import models
# 新增
from django.contrib import admin
# Create your models here.


class Vendor(models.Model):
    # 由於沒有設定PK，系統自動設定PK為 id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=20)  # 攤販的名稱
    store_name = models.CharField(max_length=10)  # 攤販店家的名稱
    phone_number = models.CharField(max_length=20)  # 攤販的電話號碼
    address = models.CharField(max_length=100)  # 攤販的地址

    # 複寫__str__ 讓回傳時更有可讀性
    def __str__(self):
        return self.vendor_name

# 新增
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    # 名稱不可更改成別的，否則Django無法辨識
    # list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']
    # 同等上面的
    list_display = [field.name for field in Vendor._meta.fields]


class Food(models.Model):
    # 由於沒有設定PK，系統自動設定PK為 id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length = 30) # 食物名稱
    price_name = models.DecimalField(max_digits=3, decimal_places=0) # 食物價錢
    food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的

    # 複寫__str__ 讓回傳時更有可讀性
    def __str__(self):
        return self.food_name



# 新增
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    # 名稱不可更改成別的，否則Django無法辨識
    list_display = ['id', 'food_name', 'price_name', 'food_vendor']
    list_filter = ('price_name',)