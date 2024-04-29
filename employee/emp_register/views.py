from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .forms import EmployeeForm, EmployeeUpdate
from .models import Employee
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_control, cache_page

# @cache_page(60 * 15)
# Create your views here.

# def cached(request):
#     user_model = get_user_model()
#     all_users = user_model.objects.all()
#     return HttpResponse('<html><body><h1>{0} users.. cached</h1></body></html>'.format(len(all_users)))

# def cacheless(request):
#     user_model = get_user_model()
#     all_users = user_model.objects.all()
#     return HttpResponse('<html><body><h1>{0} users.. cacheless</h1></body></html>'.format(len(all_users)))

# @cache_control(public = True, max_age = 3000)
# @cache_page(60 * 15)
def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request, "emp_register/employee_list.html", context)
    # return redirect(reverse('employee_list'))

# @cache_control(public = True, max_age = 3000)
# @cache_page(60 * 15)
# @require_http_methods(["GET", "POST"])
def employee_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance = employee)
        return render(request, "emp_register/employee_form.html",{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/list')

# @cache_control(public = True, max_age = 3000)
# @cache_page(60 * 15)

def employee_delete(request,id):
    if request.method == "POST":
        employee = Employee.objects.get(pk = id)
        employee.delete()
        return redirect('/list')

def add(request, a,b):
    return HttpResponse(int(a)+int(b))

@require_http_methods(["GET", "POST"])
def employee_update(request,id):
    
    if request.method == "GET":
        employee = Employee.objects.get(pk = id)
        form = EmployeeUpdate(instance = employee)
        return render(request, "emp_register/employee_update.html",{'form':form})
    else:
        if request.method == "POST":
            employee = Employee.objects.get(pk = id)
            form = EmployeeUpdate(request.POST, instance = employee)
            # HttpResponse(render(request,"emp_register/employee_update.html",{'form':form}))
            if form.is_valid():
                form.save()
            return redirect('/list')
