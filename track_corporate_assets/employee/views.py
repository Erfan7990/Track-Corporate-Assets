from django.shortcuts import render, redirect
from .models import *
from .forms import *
from company.models import *
from track_corporate_assets import settings
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

# SSL-commerz payment gatway
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class Employees_Comment(TemplateView):
    def get(self, request, *args, **kwargs):
        device_Feedback = DeviceFeedBackForm()
        Payment_Form = PaymentForm()
        
        context = {
            'device_feedback_form': device_Feedback,
            'Payment_Form': Payment_Form
        }

        
        return render(request, 'employee/payment.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            device_Feedback = DeviceFeedBackForm(request.POST)
            Payment_Form = PaymentForm(request.POST)
            if device_Feedback.is_valid() and Payment_Form.is_valid():
                device_Feedback.save()
                pay_method = Payment_Form.save()
                
                if pay_method.payment_method == 'SSLcommerz':
                    storeID = settings.STORE_ID
                    storePASS = settings.STORE_PASS

                    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=storeID, sslc_store_pass=storePASS)
                    status_url = request.build_absolute_uri(reverse('status'))
                    # mypayment.set_urls(success_url='employee/success.html', fail_url='employee/fali.html', cancel_url='employee/cancel.html', ipn_url='employee/success.html')
                    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
                    
                    device = Device.objects.filter(user = request.user)[0]
                    price = device.price
                    mypayment.set_product_integration(total_amount=Decimal(price), currency='BDT', product_category='clothing', product_name='XYZ', num_of_item=1, shipping_method='Courier', product_profile='None')
                    
                    employee_obj = Employee.objects.filter(user = request.user, is_paid = False)[0]
                    mypayment.set_customer_info(name=employee_obj.name, email=employee_obj.email, address1=employee_obj.address, address2=employee_obj.address, city=employee_obj.city, postcode=employee_obj.zipcode, country=employee_obj.country, phone=employee_obj.phone)
                    mypayment.set_shipping_info(shipping_to=employee_obj.address, address=employee_obj.address, city=employee_obj.city, postcode=employee_obj.zipcode, country=employee_obj.country)
                    response_data = mypayment.init_payment()
                    
                    return redirect(response_data['GatewayPageURL'])
            
                return redirect('index')
    

@csrf_exempt
def sslc_status(request):
    if request.method == 'POST':
        payment_data = request.POST
        
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            
            print("=========================>>>>>>")
            print(val_id)
            print(tran_id)
            print("=========================>>>>>>")
            
            return HttpResponseRedirect(reverse('sslc_complete', kwargs={'val_id':val_id, 'tran_id':tran_id}))
    return render(request, 'status.html')


def sslc_complete(request, val_id, tran_id):
    # return HttpResponse(val_id)
    
    employee_qs = Employee.objects.filter(is_paid = False)
    employee_qs = employee_qs[0]
    employee_qs.is_paid = True
    employee_qs.PaymentID = tran_id
    employee_qs.ReturnID = val_id
    employee_qs.save()
    
    return redirect('index')

