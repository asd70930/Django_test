from django.shortcuts import render
from datetime import datetime
# Create your views here.


def tv_page(request, tv=0):
    now = datetime.now()
    tv_list = [
        {"name": "瘋狗國動派出所", "tv_code": "u-GhlbyGtN4"},
        {"name": "哥哥呀哥哥", "tv_code": "jgbXe-9u10g"}
    ]
    tvno = tv
    tv_ob = tv_list[tvno]
    return render(request, 'signin/tv_page.html', locals())
