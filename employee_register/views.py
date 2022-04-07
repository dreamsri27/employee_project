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
        return redirect("employee_list")
    
    return render(request,"employee_register/employee_form.html")
def deleteemp(request,id):
    varr = Employee.objects.get(id=id)
    varr.delete()   
    return redirect("employee_list")

def editemp(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        empcode = request.POST.get('empcode')
        mobile = request.POST.get('mobile')
        position = request.POST.get('position')
        print(fullname)
        
    return redirect('employee_list')

def partiform(request,id):
    gf = Employee.objects.get(id=id)
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        empcode = request.POST.get('empcode')
        mobile = request.POST.get('mobile')
        position = request.POST.get('position')
        gf.fullname=fullname
        gf.empcode= empcode
        gf.mobile = mobile
        gf.position = position
        gf.save()
    return render(request,'employee_register/partiform.html',{'gf':gf})

