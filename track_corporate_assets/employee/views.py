from django.shortcuts import render, redirect
from .models import *
from .forms import *
from company.models import *
from track_corporate_assets import settings
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# SSL-commerz payment gatway
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def Employee_DeviceReturn(request):
    forms = DeviceReturnForm()
    employee_obj = Employee.objects.filter(user = request.user, is_paid = False)
    if request.method == 'POST':
        forms = DeviceReturnForm(request.POST)
        if forms.is_valid():
            forms.save()
            
            if forms.payment_method == 'SSLcommerz':
                storeID = settings.STORE_ID
                storePASS = settings.STORE_PASS

                mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=storeID, sslc_store_pass=storePASS)
                status_url = request.build_absolute_uri(reverse('status'))
                mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
                
                device = Device.objects.filter(user = request.user)[0]
                price = device.price
                mypayment.set_product_integration(total_amount=Decimal(price), currency='BDT', product_category='clothing', product_name='XYZ', num_of_item=1, shipping_method='Courier', product_profile='None')
                
                employee_obj = Employee.objects.filter(user = request.user, is_paid = False)
                mypayment.set_customer_info(name=employee_obj.name, email=employee_obj.email, address1=employee_obj.address, address2=employee_obj.address, city=employee_obj.city, postcode=employee_obj.zipcode, country=employee_obj.country, phone=employee_obj.phone)
                mypayment.set_shipping_info(shipping_to=employee_obj.address, address=employee_obj.address, city=employee_obj.city, postcode=employee_obj.zipcode, country=employee_obj.country)
                response_data = mypayment.init_payment()
                
                return redirect(response_data['GatewayPageURL'])
            return redirect('index')
    context = {
        'forms' : forms
    }
    
    return render(request, 'employee/payment.html', context)

@csrf_exempt
def sslc_status(request):
    if request.method == 'POST':
        payment_data = request.POST
        
        print("============")
        print(payment_data)
        print("============")
        
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            
            return HttpResponseRedirect(reverse('sslc_complete', kwargs={'val_id':val_id, 'tran_id':tran_id}))
    return render(request, 'status.html')
def sslc_complete(request, val_id, tran_id):
    employee_qs = Employee.objects.filter(user =request.user, is_paid = False)
    employee_qs = employee_qs[0]
    employee_qs.is_paid = True
    employee_qs.save()
    
    return redirect('index')

