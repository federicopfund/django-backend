from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):  # new
    template_name = "about.html"


class ContactPageView(TemplateView):  # new
    template_name = "contact.html"
    
class BlogPageView(TemplateView):  # new
    template_name = "blog.html"
    
class TrabajoPageView(TemplateView):  # new
    template_name = "trabajo.html"
    
class SimulacionesPageView(TemplateView):  # new
    template_name = "simulaciones.html"