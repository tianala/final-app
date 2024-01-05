from django.urls import path
from . import views
from .views import (
    home, CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView, CustomerDetailView,
    ShippingAddressListView, ShippingAddressUpdateView, ShippingAddressDeleteView, ShippingAddressDetailView,
    CartListView
)

urlpatterns = [
    path('', home, name='home'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreateView.as_view(), name='create-customer'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='edit-customer'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete-customer'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='create-product'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit-product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete-product'),

    # path('product/<int:product_id>/', product_detail, name='product-detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('decrease-quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease-quantity'),
    path('increase-quantity/<int:cart_item_id>/', views.increase_quantity, name='increase-quantity'),

    # Order URLs
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='create-order'),
    path('orders/<int:pk>/edit/', OrderUpdateView.as_view(), name='edit-order'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='delete-order'),

    # ShippingAddress URLs
    path('shippingaddresses/', ShippingAddressListView.as_view(), name='shippingaddress-list'),
    # path('shippingaddresses/<int:shippingaddress_id>/', ShippingAddressDetailView.as_view(), name='shippingaddress-detail'),
    path('shippingaddresses/<int:pk>/', ShippingAddressDetailView.as_view(), name='shippingaddress-detail'),
    # path('shippingaddresses/create/', ShippingAddressCreateView.as_view(), name='create-shippingaddress'),
    path('shippingaddresses/<int:pk>/edit/', ShippingAddressUpdateView.as_view(), name='shippingaddress-edit'),
    path('shippingaddresses/<int:pk>/delete/', ShippingAddressDeleteView.as_view(), name='shippingaddress-del'),
]
