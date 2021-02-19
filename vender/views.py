from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm
# Create your views here.


def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {"vendor_list": vendor_list}
    return render(request, 'vender/vendor_detail.html', context)

# 針對 vendor_create.html
def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "vendors/vendor_create.html", context)