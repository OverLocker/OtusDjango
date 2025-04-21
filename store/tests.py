from django.test import TestCase
from .models import Category, Product


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics", description="Electronic items")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")


class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics", description="Electronic items")
        self.product = Product.objects.create(name="Smartphone", description="Latest model smartphone", price=699.99,
                                              category=self.category)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Smartphone")
        self.assertEqual(self.product.price, 699.99)