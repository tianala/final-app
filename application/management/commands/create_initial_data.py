from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import Customer, Product, Order, OrderItem, ShippingAddress, Payment

class Command(BaseCommand):
    help = 'Creates initial data for application'

    def handle(self, *args, **options):
        # Check if data already exists
        if Customer.objects.exists() or Product.objects.exists() or Order.objects.exists():
            self.stdout.write(self.style.SUCCESS('Initial data already exists.'))
            return

        # Create customers
        customers = [
            {'name': 'Alice Doe', 'email': 'alice@example.com'},
            {'name': 'Bob Smith', 'email': 'bob@example.com'},
            {'name': 'Charlie Brown', 'email': 'charlie@example.com'},
            {'name': 'Diana Johnson', 'email': 'diana@example.com'},
            {'name': 'Edward Turner', 'email': 'edward@example.com'},
            {'name': 'Fiona White', 'email': 'fiona@example.com'},
            {'name': 'George Miller', 'email': 'george@example.com'},
            {'name': 'Hannah Davis', 'email': 'hannah@example.com'},
            {'name': 'Isaac Clark', 'email': 'isaac@example.com'},
            {'name': 'Julia Moore', 'email': 'julia@example.com'},
            # Add more customers as needed
            {'name': 'Kevin Anderson', 'email': 'kevin@example.com'},
            {'name': 'Linda Harris', 'email': 'linda@example.com'},
            {'name': 'Michael Wilson', 'email': 'michael@example.com'},
            {'name': 'Nancy Martin', 'email': 'nancy@example.com'},
            {'name': 'Oscar Lee', 'email': 'oscar@example.com'},
            {'name': 'Pauline Garcia', 'email': 'pauline@example.com'},
            {'name': 'Quincy Roberts', 'email': 'quincy@example.com'},
            {'name': 'Rachel Smith', 'email': 'rachel@example.com'},
            # Add more customers as needed
            # ...
        ]
        Customer.objects.bulk_create([Customer(**data) for data in customers])

        # Create electronic products
        electronic_products = [
            {'name': 'Laptop X', 'description': 'Powerful laptop with high-performance specifications.', 'price': 1499.99},
            {'name': 'Smartphone Y', 'description': 'Feature-packed smartphone with the latest technology.', 'price': 899.99},
            # Add more electronic products as needed
            # ...
        ]
        Product.objects.bulk_create([Product(**data) for data in electronic_products])

        # Create orders
        orders = [
            {'order_date': timezone.now(), 'customer': Customer.objects.get(name='Alice Doe')},
            {'order_date': timezone.now(), 'customer': Customer.objects.get(name='Bob Smith')},
            # Add more orders as needed
            # ...
        ]
        Order.objects.bulk_create([Order(**data) for data in orders])

        # Create order items
        order_items = [
            {'order': Order.objects.get(customer__name='Alice Doe'), 'product': Product.objects.get(name='Laptop X'), 'quantity': 2, 'unit_price': 1499.99},
            {'order': Order.objects.get(customer__name='Bob Smith'), 'product': Product.objects.get(name='Smartphone Y'), 'quantity': 1, 'unit_price': 899.99},
            # Add more order items as needed
            # ...
        ]
        OrderItem.objects.bulk_create([OrderItem(**data) for data in order_items])

        # Create shipping addresses
        shipping_addresses = [
            {'order': Order.objects.get(customer__name='Alice Doe'), 'address': '789 Pine St', 'city': 'City C', 'state': 'State C', 'zipcode': '56789', 'country': 'Country C'},
            {'order': Order.objects.get(customer__name='Bob Smith'), 'address': '101 Oak St', 'city': 'City D', 'state': 'State D', 'zipcode': '34567', 'country': 'Country D'},
            # Add more shipping addresses as needed
            # ...
        ]
        ShippingAddress.objects.bulk_create([ShippingAddress(**data) for data in shipping_addresses])

        # Create payments
        payments = [
            {'order': Order.objects.get(customer__name='Alice Doe'), 'payment_date': timezone.now(), 'amount': 2999.98, 'payment_method': 'Credit Card'},
            {'order': Order.objects.get(customer__name='Bob Smith'), 'payment_date': timezone.now(), 'amount': 899.99, 'payment_method': 'PayPal'},
            # Add more payments as needed
            # ...
        ]
        Payment.objects.bulk_create([Payment(**data) for data in payments])

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))
