from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("prod_id","prod_name","issue_date","included_services")

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("service_no","service_name","price")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','dob','address','phone','email','password']

