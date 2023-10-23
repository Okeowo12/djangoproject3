from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length = 15)
    img = models.ImageField(upload_to='uploads/')
    
    #class meta:
      ##  db_table = 'employee'
class Project(models.Model):
  #unique_identifier = models.CharField(max_length=50, primary_key=True)
  CATEGORY_CHOICES = [
    ("tech", "Technology"),
    ("food", "Food"),
    ("travel", "Travel")

  ]

  projecttitle = models.CharField(max_length=100)
  category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, null =True)
  approveddate =models.DateTimeField(auto_now_add=False, blank=True)
  startdate = models.DateTimeField(auto_now_add=True,blank=True)
  enddate = models.DateTimeField(auto_now_add=False,blank=True)
  projectcost=(models.FloatField)


  employee= models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)


class Department(models.Model):
  CATEGORY_CHOICES = [
    ('tech', 'Technology'),
    ('food', 'Food'),
    ('travel', 'Travel'),  
    
  ]

  departmenttitle = models.CharField(max_length=100)
  category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, null =True)
  approveddate =models.DateTimeField(auto_now_add=False, blank=True)
  startdate = models.DateTimeField(auto_now_add=True,blank=True)
  enddate = models.DateTimeField(auto_now_add=False,blank=True)
  Totalearnings=(models.FloatField)
  

  employee =models.OneToOneField(Employee,on_delete=models.CASCADE, null=True)

  #implementing many-to-one.

class Customer(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()

  def __str__(self):
    return self.name

   
   ##implementing a Customer to many orders.

class Order(models.Model):

  CATEGORY_PRODUCT = [
    ('TV', 'LG Plasma'),
    ('MV', 'Micro Wave'),
    ('FR', 'Freezer'),  
    
  ]

  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  product = models.CharField(max_length=50, choices=CATEGORY_PRODUCT, null =True)  
  order_date = models.DateTimeField(auto_now_add=True)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"Order #{self.id} by {self.customer}"