from django.db import models
import datetime
from decimal import Decimal

    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name

class Employee(models.Model):
    em_id = models.CharField(max_length=100,unique=True,primary_key=True) #id เดียวกันกับ dependent
    em_name = models.CharField(max_length=100)
    em_phone = models.CharField(max_length=100)
    em_address = models.CharField(max_length=100)
    em_mail = models.CharField(max_length=100)

    def __str__(self):
        return self.em_id + self.em_name + self.em_phone + self.em_address + self.em_mail

class Dependent(models.Model):
    d_id = models.CharField(max_length=100,primary_key=True) #id เดียวกันกับ employee
    d_name = models.CharField(max_length=100)
    d_relation = models.CharField(max_length=100)
    d_phone = models.CharField(max_length=100)

    def __str__(self):
        return self.d_id + self.d_name + self.d_relation + self.d_phone

class Customer(models.Model):
    c_id = models.CharField(max_length=100,primary_key=True)
    c_name = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=100)
    c_address = models.CharField(max_length=100)
    c_mail = models.CharField(max_length=100)

    def __str__(self):
        return self.c_id + " - " + self.c_name #+ self.c_phone + self.c_address + self.c_mail

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	#@daverobb2011
	class Meta:
		verbose_name_plural = 'categories'

class Category1(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	#@daverobb2011
	class Meta:
		verbose_name_plural = 'types of food'
        
class Product(models.Model):
    p_id = models.CharField(max_length=100,primary_key=True)
    p_name = models.CharField(max_length=100) #บอกสูตรอาหารให้ครบในชื่อ
    p_company = models.CharField(max_length=100) #ชื่อผู้ผลิต
    p_price = models.IntegerField()
    p_number = models.IntegerField() #จำนวนสินค้าคงเหลือ
    p_type = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    p_cat = models.ForeignKey(Category1, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.p_id + " - " + self.p_name 


class Receipt(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tprice = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.tprice = self.quantity * self.product.p_price
        self.total_amount = Decimal(self.tprice)  # Convert to Decimal
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.c_name} - {self.product.p_name}"

class ReceiptProduct(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    #total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.product.p_price
        super().save(*args, **kwargs)


#



