# application/models.py
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
class ElectronicProductImage(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='product_images/')

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    electronic_product_image = models.ForeignKey(ElectronicProductImage, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     def __str__(self):
#         return self.name
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart"
    
class Order(BaseModel):
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.order_date}"

class ShippingAddress(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"ShippingAddress {self.id} - {self.order}"

class Payment(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment {self.id} - {self.order}"
