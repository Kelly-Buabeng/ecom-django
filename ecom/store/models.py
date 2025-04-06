from django.db import models
import datetime


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Customer(models.Model):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  
    email = models.EmailField()
    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=250, default='',blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product