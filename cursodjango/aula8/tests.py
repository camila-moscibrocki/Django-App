from django.test import TestCase

class SimpleTest(TestCase):
    def test_sum(self):
        self.assertEqual(sum([2, 2]), 4)

    def test_foo(self):
        nome = "Camila"

        self.assertIn("mila", nome)