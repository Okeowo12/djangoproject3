from django import forms
from crudapp.models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = "__all__"  
        widgets ={
            'approveddate': forms.SelectDateWidget(),
            'enddate':forms.SelectDateWidget(),
        } 
           
class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = "__all__"  
        widgets ={
            'approveddate': forms.SelectDateWidget(),
            'enddate':forms.SelectDateWidget(),
       }  

class CustomerForm(forms.ModelForm):

    class Meta:
        model =Customer
        fields = "__all__" 

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__" 
        