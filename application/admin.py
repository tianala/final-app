# application/admin.py
from django.contrib import admin
from .models import Customer, Product, Order, ShippingAddress, Payment, Cart

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'customer']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'address', 'city', 'state', 'zipcode', 'country']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_date', 'amount', 'payment_method']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']