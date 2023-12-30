# application/forms.py
from django import forms
from .models import Customer, Product, Order, OrderItem, ShippingAddress, Payment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'customer']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'unit_price']

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['order', 'address', 'city', 'state', 'zipcode', 'country']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'payment_date', 'amount', 'payment_method']
