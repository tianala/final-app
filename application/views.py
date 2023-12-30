# Order views
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from .forms import CustomerForm, ProductForm, OrderForm, OrderItemForm, ShippingAddressForm, PaymentForm
from .models import Customer, Product, Order, OrderItem, ShippingAddress, Payment
# application/views.py
# application/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'application/customer_list.html'
    paginate_by = 10

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'application/create_customer.html'
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'application/edit_customer.html'
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'application/delete_customer.html'
    success_url = reverse_lazy('customer-list')
    

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 10

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_del.html'
    success_url = reverse_lazy('product-list')
    
class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'application/order_list.html'
    paginate_by = 10

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'application/create_order.html'
    success_url = reverse_lazy('order-list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'application/edit_order.html'
    success_url = reverse_lazy('order-list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'application/delete_order.html'
    success_url = reverse_lazy('order-list')

# OrderItem views
class OrderItemListView(ListView):
    model = OrderItem
    context_object_name = 'order_items'
    template_name = 'application/orderitem_list.html'
    paginate_by = 10

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'application/create_orderitem.html'
    success_url = reverse_lazy('orderitem-list')

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'application/edit_orderitem.html'
    success_url = reverse_lazy('orderitem-list')

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'application/delete_orderitem.html'
    success_url = reverse_lazy('orderitem-list')

# ShippingAddress views
class ShippingAddressListView(ListView):
    model = ShippingAddress
    context_object_name = 'shipping_addresses'
    template_name = 'application/shippingaddress_list.html'
    paginate_by = 10

class ShippingAddressCreateView(CreateView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'application/create_shippingaddress.html'
    success_url = reverse_lazy('shippingaddress-list')

class ShippingAddressUpdateView(UpdateView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'application/edit_shippingaddress.html'
    success_url = reverse_lazy('shippingaddress-list')

class ShippingAddressDeleteView(DeleteView):
    model = ShippingAddress
    template_name = 'application/delete_shippingaddress.html'
    success_url = reverse_lazy('shippingaddress-list')

# Payment views
class PaymentListView(ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'application/payment_list.html'
    paginate_by = 10

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'application/create_payment.html'
    success_url = reverse_lazy('payment-list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'application/edit_payment.html'
    success_url = reverse_lazy('payment-list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'application/delete_payment.html'
    success_url = reverse_lazy('payment-list')
