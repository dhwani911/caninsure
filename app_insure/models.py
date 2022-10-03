import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    """Available products list for admin panel"""
    prod_name = models.CharField(max_length=100)
    issue_date = models.DateField(auto_now_add=True)
    prod_id = models.CharField(max_length=200)
    included_services = models.IntegerField(default=True)

    # creating customized product id
    @property
    def prod_id(self):
        return "".join(self.prod_name[:1]+str(self.issue_date.isoformat()).replace("-","")[2:6]+ str(self.included_services)) if self.prod_name else '-'

    def __str__(self):
        return self.prod_name

class Services(models.Model):
    """Services offered which is maintained from service panel"""
    service_no = models.ForeignKey(Products,max_length=100,default=True,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)

    # Creating customized service no based on product_id
    @property
    def service_no(self):
        products = Products.objects.all()
        for i in products:
            return str(i.prod_id)[1:5] + str(i.included_services) + str(self.id)

    def __str__(self):
        return self.service_name

    def validation_services(self):
        products = Products.objects.all()
        for i in products:
            if self.service_no[-1] > i.included_services:
                break


class Client(models.Model):
    """User register list"""
    name = models.CharField(max_length=255)
    dob = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

