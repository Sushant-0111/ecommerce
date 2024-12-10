from django.contrib import admin
from .models import Category
from .models import Product
from .models import Customer
from .models import cart
from .models import cart_Item
from .models import Order
# Register your models here.

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display =['name']
    search_fields=[
       'name','Category'
       
   ]

@admin.register(Product)
class Product(admin.ModelAdmin):
   list_display =[
       'name', 
       'price',
       'qty', 
       'category'
   ]
   list_filter =[
       'category'
   ]
   search_fields=[
       'name','category'
       
   ]
   list_per_page = 20
   autocomplete_fields=['category']


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = [
        "first_name", 
        "middle_name",
        "last_name",
        "contact",
        "address",

    ]



class cartItemInline(admin.StackedInline):
    model = cart_Item
    extra = 2



@admin.register(cart)
class cart(admin.ModelAdmin):
    list_display = [
        "customer",
    ]
    
    inlines = [
        cartItemInline,
    ]
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "address",
        "payment_status",
        "payment_mode",
        "status",
        ]
    list_editable = ["status"]
    list_filter =  ["payment_status", "payment_mode", 'status']
