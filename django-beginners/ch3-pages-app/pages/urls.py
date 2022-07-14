from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BlogPageView,TrabajoPageView,SimulacionesPageView # new

urlpatterns = [
    path("simulaciones/", SimulacionesPageView.as_view(), name="simulaciones"), # new
    path("trabajo/", TrabajoPageView.as_view(), name="trabajo"), # new
    path("blog/", BlogPageView.as_view(), name="blog"), # new
    path("contact/", ContactPageView.as_view(), name="contact"), # new
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("", HomePageView.as_view(), name="home"),
]
