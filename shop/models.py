from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=60)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=200)
    launch_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    person_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=12,default="")
    desc=models.CharField(max_length=500,default=0)

    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=50) 
    email=models.CharField(max_length=50) 
    address=models.CharField(max_length=150) 
    city=models.CharField(max_length=50) 
    state=models.CharField(max_length=50) 
    pincode=models.CharField(max_length=6)
    phone=models.CharField(max_length=12,default="") 

    def __str__(self):
         return str(self.order_id) 

class orderUpdate(models.Model):
    order_id=models.AutoField(primary_key=True)
    update_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=2000)
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[:10] + "...."


