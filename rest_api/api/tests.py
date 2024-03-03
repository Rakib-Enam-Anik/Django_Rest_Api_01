from django.test import TestCase

# Create your tests here.


def add(a,b):
    return a+b

class TestAddTwoValue(TestCase):
    def test_add(self):
        sum = add(3,5)
        print(sum)
        self.assertEqual(sum, 8)
