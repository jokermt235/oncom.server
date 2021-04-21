"""This test can cover all reusable code in api application
    backend authored by Mutalip
    mail: jokermt235@yandex.com
    github : https://github.com/jokermt235
"""
from django.test import TestCase
from django.core import serializers
from .models import *
from .managers import *

class TestSubcategory(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="Категория 1", desc="Описание Категории 1")
        #Create Subcategory
        self.subcategory1 = Subcategory.objects.create(name="Подкатегория 1" , 
                            desc="Описание Подкатегории 1", category=self.category)
        self.subcategory2 = Subcategory.objects.create(name="Подкатегория 2" , 
                            desc="Описание Подкатегории 2", category=self.category)

        self.shop1 = Shop.objects.create(name="Магазин 1", rating=1)
        #Create Producs
        self.product1 = Product.objects.create(name="Продукт 1", desc="Описание продукта 1", 
                        category=self.category,rating=0,price=10,discount=0,phone="123 312 3123",
                        shop=self.shop, subcategory=self.subcategory1)
        self.product2 = Product.objects.create(name="Продукт 2", desc="Описание продукта 2", 
                        category=self.category,rating=0,price=10,discount=0,phone="123 312 3123",
                        shop=self.shop1,subcategory=self.subcategory2)


    def test_get_subcategory_list_by_category(self):
        cat_id = self.category.id
        results = serializers.serialize("json", ModelManager(Subcategory).find(params = {"category_id" : cat_id}))
        self.assertIn("Подкатегория 2", results)

    def test_get_product_by_category(self):
        pass

