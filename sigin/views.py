from django.shortcuts import render
from datetime import datetime
# Create your views here.


def sigin_page(request):
    now = datetime.now()
    return render(request, "sigin/sigin.html", locals())
