from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
# Import Models
from .models import *
from employee.models import *

# Import Forms
from .forms import *
from employee.forms import *

# Create your views here.

def Index(request):
    if request.user.is_authenticated:
        Employee_Info = Employee.objects.filter(user = request.user)
        context = {
            'Employee_Info': Employee_Info
        }
        return render(request, 'company/index.html', context)
    else:
        return render(request, 'company/index.html')
def SignUp(request):
    signupForm = SignUpForm()
    
    try:
        if request.method == 'POST':
            signupForm = SignUpForm(request.POST)
            if signupForm.is_valid():
                signupForm.save()
                
                messages.success(request, 'Account Created Successfully')
                return HttpResponseRedirect(request.path_info)
        else:
            signupForm = SignUpForm()
    except Exception as e:
        print(e)    
    context = {'signupForm': signupForm}
    return render(request, 'company/signup.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username)
        
        if not user_obj.exists():
            messages.warning(request, 'Account not Found')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = username, password = password)

        if user_obj is not None:
            login(request, user_obj)
            # username = User.username
            return redirect('index')
        else:
            messages.warning(request, 'Username or password is not correct')
            return HttpResponseRedirect(request.path_info)
    
        # messages.warning(request, 'Invalid Information')
        # context = { 'username': username}
    else:
        if request.user.is_superuser == True:
            messages.warning(request, 'Admin user can not login')
        
    
    return render(request, 'company/signin.html')

def logout_page(request):
    logout(request)
    return redirect('index')



# @login_required
# @permission_required('auth.view_user')
def Add_Employee(request):
    Employee_Form = EmployeeModelForm()
    if request.method == 'POST':
        device = Device.objects.filter(user = request.user)
        Employee_Form = EmployeeModelForm(request.POST)
        
        if Employee_Form.is_valid():
            Employee_Data_Form = Employee_Form.save(commit=False)
            Employee_Data_Form.user = request.user
            # device = Employee_Form.cleaned_data['device']
            # Employee_Form.device = device
            Employee_Data_Form.save()
            Employee_Form.save_m2m()
          
            return redirect('index')
    context = {
        'Employee_Form' :Employee_Form
    }
    return render(request, 'company/add_employee.html',context)
    
def add_devices(request):
    device_form = DevicesForm()
    if request.method == 'POST':       
        device_form = DevicesForm(request.POST, request.FILES)
        if device_form.is_valid():
            device_form = device_form.save(commit=False)
            device_form.user = request.user
            device_form.save()
            messages.success(request, 'Save Successfully !!')
            return HttpResponseRedirect(request.path_info)
    
    context = {
        'device_form': device_form
    }
    return render(request, 'company/add_device.html', context)
