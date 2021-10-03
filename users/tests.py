from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from users.models import Couses
# Create your tests here.
pas = make_password('1234')
class UserViewTestCase(TestCase):
    def setUp(self):
        couse = Couses.objects.create(subject ="cal",term =1,couseid = 100, num_student=60, year=2021)
        couse2 = Couses.objects.create(subject ="1",term =1,couseid = 1, num_student=1, year=1)
        user = User.objects.create(username='user1' , password=pas , email='user1@example.com')

    def test_index(self):
        c= Client()
        index_response = c.get(reverse('users:index'))
        self.assertEqual(index_response.status_code, 200)
    
    def test_docouses(self):
        c= Client()
        couse = Couses.objects.get(subject="cal")
        couse.save()
        couse_response = c.get(reverse('users:couses',args=(couse.id,)))
        self.assertEqual(couse_response.status_code, 200)
    
    def test_book(self):
        c= Client()
        couse = Couses.objects.get(subject="cal")
        couse.save()
        book_response = c.get(reverse('users:book',args=(couse.id,)))

    def test_book_authenticate(self):
        c= Client()
        user = User.objects.get(username='user1')
        couse = Couses.objects.get(subject="cal")
        couse.save()
        c.force_login(user)
        book_response = c.get(reverse('users:book',args=(couse.id,)))
    
    def test_debook_authenticate(self):
        c= Client()
        user = User.objects.get(username='user1')
        couse = Couses.objects.get(subject="cal")
        couse.save()
        c.force_login(user)
        book_response = c.get(reverse('users:book',args=(couse.id,)))
        debook_response = c.get(reverse('users:debook', args=(couse.id,)))

    def test_admun(self):
        c= Client()
        user = User.objects.first()
        couse = Couses.objects.get(subject="cal")
        user.is_superuser = True
        c.force_login(user)
        user.save()
        couse.save()
        admin_response = c.get(reverse('users:admun',args=(couse.id,)))
        couse.status = False
        couse.save()
        admin_response = c.get(reverse('users:admun',args=(couse.id,)))