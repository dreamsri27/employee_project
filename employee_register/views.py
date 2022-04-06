from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import *

# Create your views here.
def employee_list(request):
    data = Employee.objects.all()

    return render(request,"employee_register/employee_list.html",{'data':data})
def employee_form(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        empcode = request.POST.get('empcode')
        mobile = request.POST.get('mobile')
        position = request.POST.get('position')
        print(fullname)
        employeedata = Employee(fullname=fullname,empcode=empcode,mobile=mobile,position=position)
        employeedata.save()

        message = "data saved succesfully"
        return render(request,'employee_register/employee_form.html',{'message':message})
    
    return render(request,"employee_register/employee_form.html")
def deleteemp(request,id):
    varr = Employee.objects.get(id=id)
    varr.delete()   
    return redirect("employee_list")

def editemp(request)

