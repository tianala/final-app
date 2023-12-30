from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import Customer, Product, Order, OrderItem, ShippingAddress, Payment

class Command(BaseCommand):
    help = 'Creates initial data for application'

    def handle(self, *args, **options):
        # Create customers
        customer1 = Customer.objects.create(name='John Doe', email='john@example.com')
        customer2 = Customer.objects.create(name='Jane Smith', email='jane@example.com')

        # Create products
        product1 = Product.objects.create(name='Product A', description='Description for Product A', price=19.99)
        product2 = Product.objects.create(name='Product B', description='Description for Product B', price=29.99)

        # Create orders
        order1 = Order.objects.create(order_date=timezone.now(), customer=customer1)
        order2 = Order.objects.create(order_date=timezone.now(), customer=customer2)

        # Create order items
        order_item1 = OrderItem.objects.create(order=order1, product=product1, quantity=2, unit_price=product1.price)
        order_item2 = OrderItem.objects.create(order=order2, product=product2, quantity=1, unit_price=product2.price)

        # Create shipping addresses
        shipping_address1 = ShippingAddress.objects.create(
            order=order1,
            address='123 Main St',
            city='City A',
            state='State A',
            zipcode='12345',
            country='Country A'
        )

        shipping_address2 = ShippingAddress.objects.create(
            order=order2,
            address='456 Oak St',
            city='City B',
            state='State B',
            zipcode='67890',
            country='Country B'
        )

        # Create payments
        payment1 = Payment.objects.create(order=order1, payment_date=timezone.now(), amount=39.98, payment_method='Credit Card')
        payment2 = Payment.objects.create(order=order2, payment_date=timezone.now(), amount=29.99, payment_method='PayPal')

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))
