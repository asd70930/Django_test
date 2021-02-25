from django.shortcuts import render
from .models import Product, Order
from django.db.models import Sum
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

def showtemplate(request):
    vendor_list = Product.objects.all()
    context = {"vendor_list": vendor_list}
    return render(request, context)


def check_vip_stock(fun):
    def wrapper(request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        product_id = received_json_data["product_id"]
        customer_is_vip = received_json_data['vip']
        product = Product.objects.get(product_id=product_id)
        product_vip = product.vip
        product_stock_pcs = product.stock_pcs
        identity_check = True
        if product_vip:
            if customer_is_vip != product_vip:
                identity_check = False
        check_result = (identity_check, product_stock_pcs)
        fun(request, check_result)
    return wrapper


def check_stock(fun):
    def wrapper(request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        product_id = received_json_data["product_id"]
        product = Product.objects.get(product_id=product_id)
        product_stock_pcs = product.stock_pcs
        check_result = product_id, product_stock_pcs
        fun(request, check_result)
    return wrapper


@csrf_exempt
@check_vip_stock
def add_order(request, check_result):
    received_json_data = json.loads(request.body.decode("utf-8"))
    identity_check, product_stock_pcs = check_result
    if not identity_check:
        return HttpResponse(json.dumps({"message": "該商品為VIP限定, 訂單失敗"}), content_type="application/json")
    customer_order_amount = received_json_data["amount"]
    if customer_order_amount > product_stock_pcs:
        return HttpResponse(json.dumps({"message": "貨源不足, 訂單失敗"}), content_type="application/json")

    remaining_stock = product_stock_pcs - customer_order_amount
    product_id = received_json_data["product_id"]
    customer_id = received_json_data["customer_id"]
    Product.objects.filter(product_id=product_id).update(stock_pcs=remaining_stock)
    order = Order(product_id=product_id, qty=customer_order_amount, customer_id=customer_id)
    order.save()
    ##
    # html 產生 交由前端JQ渲染
    html = ""
    print('done')
    ##
    return HttpResponse(json.dumps({"message": "貨源不足, 訂單失敗", "html": html}), content_type="application/json")

@csrf_exempt
@check_stock
def delete_order(request, check_result):
    received_json_data = json.loads(request.body.decode("utf-8"))
    product_id, remain_stock = check_result
    product_stock_pcs = remain_stock
    order_id = received_json_data['order_id']
    order = Order.objects.get(id=order_id)
    order_qty = order.qty
    update_stock = remain_stock + order_qty
    Order.objects.get(id=order_id).delete()
    Product.objects.filter(product_id=product_id).update(stock_pcs=update_stock)
    return HttpResponse(json.dumps({"message": "訂單刪除成功"}), content_type="application/json")

@csrf_exempt
def show_top(request):
    orders = Order.objects.values('product_id').annotate(qty=Sum('qty')).order_by('-qty')[:3]
    return HttpResponse(json.dumps({"orders": orders}), content_type="application/json")


