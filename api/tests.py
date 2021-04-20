from django.test import TestCase
from django.core import serializers
from .models import *
from .managers import *
# Create your tests here.

class TestSubcategory(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="Категория 1", desc="Описание Категории 1")
        Subcategory.objects.create(name="Подкатегория 1" , 
                            desc="Описание Подкатегории 1", category=self.category)
        Subcategory.objects.create(name="Подкатегория 2" , 
                            desc="Описание Подкатегории 2", category=self.category)

    def test_get_subcategory_list_by_category(self):
        cat_id = self.category.id
        results = serializers.serialize("json", ModelManager(Subcategory).find(params = {"category_id" : cat_id}))
        self.assertIn("Подкатегория 2", results)

