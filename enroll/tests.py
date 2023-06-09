from django.test import TestCase, RequestFactory
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


class HomeViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get('/home')
        response = render(request, 'enroll/home.html', {'form': StudentRegistration(), 'stud': User.objects.all()})

        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'enroll/home.html')
        self.assertContains(response, '<form')
        # self.assertContains(response, 'method="post"')



