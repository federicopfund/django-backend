from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>página principal</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")

class ContactpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h1>Contact</h1>")
        
class BlogPageView(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("blog"))
        self.assertTemplateUsed(response, "blog.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("blog"))
        self.assertContains(response, "<h1>blog</h1>")
            
class TrabajospageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/trabajos/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("trabajos"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("trabajos"))
        self.assertTemplateUsed(response, "trabajos.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("trabajos"))
        self.assertContains(response, "<h1>Trabajos</h1>")
        
class SimulacionesPageView(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/simulaciones/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("simulaciones"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("simulaciones"))
        self.assertTemplateUsed(response, "simulaciones.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("simulaciones"))
        self.assertContains(response, "<h1>Simulaciones Empresariales</h1>")