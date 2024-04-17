from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
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

# @cache_control(public = True, max_age = 3000)
# @cache_page(60 * 15)
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
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('/list')
