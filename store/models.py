from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class SharedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
 

class Category(SharedModel):
        name  = models.CharField(max_length=50)

        def __str__(self):
            return self.name


class Product(SharedModel):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    qty = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} price{self.price}"



class Customer(SharedModel):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=10, null=True , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"



class cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f" cart of {self.customer}"
    
class cart_Item(SharedModel):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    qty = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product
    
    def __str__(self):
        return f"{self.cart.customer} {self.product}"
    
class Order(SharedModel):
    ORDER_PENDING_CHOICES = "PENDING"
    ORDER_INDELIVERY_CHOICES = "INDELIVERY"
    ORDER_COMPLETED_CHOICES = "COMPLETED"
    ORDER_STATUS = [
        (ORDER_PENDING_CHOICES, 'PENDING'),
        (ORDER_COMPLETED_CHOICES, 'COMPLETED'),
        (ORDER_INDELIVERY_CHOICES, 'INDELIVERY')
    ]
    PAYMENT_MODE_KHALTI = "KHALTI" 
    PAYMENT_MODE_COD= "COD" 
    PAYMENT_MODE = [
        (PAYMENT_MODE_KHALTI, 'PENDING'),
        (PAYMENT_MODE_COD, 'COD')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    address = models.CharField(max_length=255 , null =True , blank = True)
    payment_status = models.BooleanField(default = False)
    payment_mode = models.CharField(max_length=255,choices=PAYMENT_MODE)
    status = models.CharField(max_length=255, choices= ORDER_STATUS, default=ORDER_PENDING_CHOICES) 

    def __str__(self):
        return f" OrderID #{self.pk} "


class order_Item(SharedModel):
    order = models.ForeignKey(cart, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product
