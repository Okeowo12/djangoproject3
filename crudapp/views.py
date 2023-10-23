from django.shortcuts import render,redirect
from crudapp.forms import  *
from crudapp.models import Employee  
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Employee data saved successfully!")
                return render(request, 'crudapp/index.html', {'form':form})
            except Exception as e:
                messages.error(request, f"An error occured: {str(e)}") 

    else:
        form = EmployeeForm()  
    return render(request, 'crudapp/index.html', {'form': form})                 
    




def show(request):  
    employees = Employee.objects.all().order_by("-id")  
    return render(request,'crudapp/show.html',{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'crudapp/edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show/")  
    return render(request, 'crudapp/edit.html', {'employee': employee})  

def delete(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show/")  

def deactivate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.is_active:
        user.is_active = False
        user.save()
        # You might want to add a success message here
    else:
        # User is already deactivated
        pass

    # Redirect or render a template


def project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Project saved successfully!")
                return render(request, 'crudapp/project.html', {'form':form})
            except Exception as e:
                messages.error(request, f"An error occured: {str(e)}") 

    else:
        form = ProjectForm()  
    return render(request, 'crudapp/project.html', {'form': form}) 



def department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "saved successfully!")
                return render(request, 'crudapp/department.html', {'form':form})
            except Exception as e:
                messages.error(request, f"An error occured: {str(e)}") 

    else:
        form = DepartmentForm()  
    return render(request, 'crudapp/department.html', {'form': form}) 


def departmentlab(request):  
    departments = Department.objects.all().order_by("-id")  
    return render(request,'crudapp/departmentlab.html',{'departments':departments})  




def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Customer order saved successfully!")
                return render(request, 'crudapp/order.html', {'form':form})
            except Exception as e:
                messages.error(request, f"An error occured: {str(e)}") 

    else:
        form = OrderForm()  
    return render(request, 'crudapp/order.html', {'form': form})  



def customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Customer details saved successfully!")
                return render(request, 'crudapp/customer.html', {'form':form})
            except Exception as e:
                messages.error(request, f"An error occured: {str(e)}") 

    else:
        form = CustomerForm()  
    return render(request, 'crudapp/customer.html', {'form': form})  

def showcustomerorder (request):  
    customer = Order.objects.all().order_by("-id")  
    return render(request,'crudapp/showcustomerorder.html',{'customer':customer})  
  