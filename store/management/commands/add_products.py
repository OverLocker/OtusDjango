from django.core.management.base import BaseCommand
from store.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        category = Category.objects.create(name='Electronics', description='Electronic items')
        Product.objects.create(name='Smartphone', description='Latest model smartphone', price=699.99, category=category)
        Product.objects.create(name='Laptop', description='High performance laptop', price=999.99, category=category)