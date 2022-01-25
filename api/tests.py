"""This test can cover all reusable code in api application
    backend authored by Mutalip
    mail: jokermt235@yandex.com
    github : https://github.com/jokermt235
"""
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from django.core import serializers
from .models import *
from .managers import *

"""class TestFilterByCategoryAndSubcategory(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="Категория 1", desc="Описание Категории 1")
        self.category2 = Category.objects.create(name="Категория 2", desc="Описание Категории 2")
        self.user = User.objects.create_user(username="vasya", email="vasya@mail.ru" ,password="123456")
        #Create Subcategory
        self.subcategory1 = Subcategory.objects.create(name="Подкатегория 1" , 
                            desc="Описание Подкатегории 1", category=self.category)
        self.subcategory2 = Subcategory.objects.create(name="Подкатегория 2" , 
                            desc="Описание Подкатегории 2", category=self.category)

        self.shop1 = Shop.objects.create(name="Магазин 1", rating=1, user=self.user)
        self.product1 = Product.objects.create(name="Продукт 1", desc="Описание продукта 1", 
                        category=self.category,rating=0,user=self.user, price=10,
                        discount=0,phone="0312 312 3121",
                        shop=self.shop1, subcategory=self.subcategory1)
        self.product2 = Product.objects.create(name="Продукт 2", desc="Описание продукта 2", 
                        category=self.category,rating=0,user=self.user,
                        price=10,discount=0,phone="0312 312 3122",
                        shop=self.shop1,subcategory=self.subcategory2)
        self.product3 = Product.objects.create(name="Продукт 3", desc="Описание продукта 3", 
                        category=self.category2,rating=0,user=self.user,
                        price=10,discount=0,phone="0312 312 3123",
                        shop=self.shop1,subcategory=self.subcategory1)

    def test_get_subcategory_list_by_category(self):
        cat_id = self.category.id
        results = serializers.serialize("json", ModelManager(Subcategory).find(params = {"category_id" : cat_id}))
        self.assertIn("Подкатегория 2", results)

    def test_get_product_by_category(self):
        cat_id = self.category.id
        results = serializers.serialize("json", ModelManager(Product).find(params = {"category_id" : cat_id}))
        self.assertIn("Продукт 1", results)

    def test_get_product_by_subcategory(self):
        sub_cat_id = self.subcategory2.id
        results = serializers.serialize("json", ModelManager(Product).find(params = {"subcategory_id" : sub_cat_id}))
        self.assertIn("Продукт 2", results)
    

    def test_get_product_by_category_and_subcategory(self):
        cat_id     = self.category2.id
        sub_cat_id = self.subcategory1.id
        results = serializers.serialize("json", ModelManager(Product).find(params = {"category_id" : cat_id, "subcategory_id" : sub_cat_id}))
        self.assertIn("Продукт 3", results)


class TestUserShopAndUserProducts(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(username="vasya1", email="vasya1@mail.ru" ,password="123456")
        self.user2 = User.objects.create_user(username="vasya2", email="vasya2@mail.ru" ,password="123456")
        self.shop1 = Shop.objects.create(name="Магазин 1", rating=1, user=self.user1)
        self.shop2 = Shop.objects.create(name="Магазин 2", rating=1, user=self.user1)
        self.shop3 = Shop.objects.create(name="Магазин 3", rating=1, user=self.user2)
        self.shop4 = Shop.objects.create(name="Магазин 4", rating=1, user=self.user2)

    def test_get_shoplist_of_user(self):
        user_id = self.user1.id
        results = serializers.serialize("json", ModelManager(Shop).find(params = {"user_id" : user_id}))
        self.assertIn("Магазин 1" , results)
        self.assertIn("Магазин 2" , results)
        user_id2 = self.user2.id
        results = serializers.serialize("json", ModelManager(Shop).find(params = {"user_id" : user_id2}))
        self.assertIn("Магазин 3" , results)
        self.assertIn("Магазин 4" , results)

    def test_allow_user_update_belonged_shop(self):
        user_id = self.user1.id
        shops = ModelManager(Shop).find(params={"user_id" : user_id})
        for shop in shops:
            shop.name = shop.name  + " updated"
            shop.save()
        results = serializers.serialize("json", ModelManager(Shop).find(params = {"user_id" : user_id}))
        self.assertIn("Магазин 2" , results)
        self.assertIn("updated" , results)
"""

class TestPincode(TestCase):
    def setUp(self)-> None:
        self.user1 = User.objects.create_user(username="vasya1", email="vasya1@mail.ru" ,password="123456")
        self.pincode1 = Pincode.objects.create(user=self.user1,pincode=1234)

    def test_generate_pincode(self):
        user_id = self.user1.id
        result = serializers.serialize("json", ModelManager(Pincode).find(params = {"user_id": user_id}));
        self.assertIn("1234", result)
