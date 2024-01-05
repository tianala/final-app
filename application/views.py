# Order views
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import CustomerForm, ProductForm, OrderForm, ShippingAddressForm, PaymentForm
from .models import Customer, Product, Order, ShippingAddress, Payment, Cart
from django.http import JsonResponse
import json


def home(request):
    return render(request, 'home.html')


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customer_list.html'
    paginate_by = 10
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'  # Set the template name as per your project structure
    context_object_name = 'customer'
    
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'create_customer.html'
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'edit_customer.html'
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'delete_customer.html'
    success_url = reverse_lazy('customer-list')
    
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 12
    # json_file_path = 'electronics_data.json'
    json_file_path = 'application/templates/data/electronics_data.json'
    # 'home/tianala28/final-app/application/templates/data/electronics_data.json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        electronic_product_images = self.get_electronic_product_images()
        context['electronic_product_images'] = electronic_product_images
        return context

    def get_electronic_product_images(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('electronic_products', [])

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
    template_name = 'order_list.html'
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
    
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the product is already in the cart
    cart_item, created = Cart.objects.get_or_create(product=product)


    # If the product is already in the cart, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product-list')  # Adjust the URL name as needed


class CartListView(ListView):
    model = Cart
    template_name = 'cart_list.html'
    context_object_name = 'cart_items'
    paginate_by = 10

def decrease_quantity(request, cart_item_id):
    # Implement the logic to decrease the quantity for the specified cart item
    # Update your Cart model or session accordingly
    return JsonResponse({'success': True})

def increase_quantity(request, cart_item_id):
    # Implement the logic to increase the quantity for the specified cart item
    # Update your Cart model or session accordingly
    return JsonResponse({'success': True})


def your_view(request):
    # Assuming the user is authenticated, you might filter the cart items by user
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        # If the user is not authenticated, you might be using a session-based cart
        cart_count = Cart.objects.filter(session_key=request.session.session_key).count()

    return render(request, 'cart_list.html', {'cart_count': cart_count})

    
def shipping_address_detail(request, shipping_address_id):
    shipping_address = ShippingAddress.objects.get(id=shipping_address_id)
    return render(request, 'shipping_address.html', {'shipping_address': shipping_address})

class ShippingAddressDetailView(DetailView):
    model = ShippingAddress
    template_name = 'shippingaddress_detail.html'  # replace with your template file name
    context_object_name = 'shipping_address'
class ShippingAddressListView(ListView):
    model = ShippingAddress
    context_object_name = 'shipping_addresses'
    template_name = 'shippingaddress_list.html'
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
