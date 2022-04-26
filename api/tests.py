"""This test can cover all reusable code in api application
    backend authored by Mutalip
    mail: jokermt235@yandex.com
    github : https://github.com/jokermt235
"""
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.core import serializers
from .models import *
from .managers import *
from .views import *

class TestPincode(TestCase):
    def setUp(self)-> None:
        self.pincode1 = Pincode.objects.create(email="vasya1@mail.ru", pincode=1234)

    def test_generate_pincode(self):
        result = ModelManager(Pincode).find(params = {"email": "vasya1@mail.ru"})
        self.assertEqual('1234', result[0].pincode)

class TestDocument(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user1 = User.objects.create_user(username="vasya1", email="vasya1@mail.ru" ,password="123456")
        self.document1 = Document.objects.create(user=self.user1, name="document1", path='images/documents/image1.jpg', size=1024)
        self.document1 = Document.objects.create(user=self.user1, name="document2", path='images/documents/image2.jpg', size=1024)
        return super().setUp()
    def test_create_document(self):
        user_id = self.user1.id
        result = ModelManager(Document).find(params = {"user_id": user_id})
        index = 1
        for document in result:
            self.assertEqual("document" + str(index), document.name)
            self.assertEqual("images/documents/image" + str(index) + ".jpg", document.path)
            index +=1
    def test_upload_document(self):
        # setup request to pass into view
        request = self.factory.post('/document/create')
        # A request requies user 
        request.user = self.user1
        # As View takes onlye two params a method and action
        response = DocumentCreateView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)

class TestUserupdate(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(username="vasya1", email="vasya1@mail.ru",password="123456")
        return super().setUp()
    def test_user_update(self):
            self.assertEqual("a", "b")