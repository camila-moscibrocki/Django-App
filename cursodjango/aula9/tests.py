from django.test import TestCase
from django.urls import reverse

class TesteIndexView(TestCase):

    def setUp(self):
        self.url = reverse("aula9")


    def test_status_code(self):
        response = self.client.get(self.url)
        import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(self.url)
        template1 = response.templates[0]
        self.assertTemplateUsed(response,"aula9/aula9.html")
        self.assertTemplateUsed(response,"base.html")

    def test_context(self):
        response = self.client.get(self.url)
        self.assertEqual("Camila", response.context("nome"))