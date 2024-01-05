# application/forms.py
from django import forms
from .models import Customer, Product, Order, ShippingAddress, Cart

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


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'state', 'zipcode', 'country']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product', 'quantity']


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)