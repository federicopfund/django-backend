from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.acercade, name='AcercaDe'),
    #path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='tiendaApp/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='tiendaApp/logout.html'), name='logout'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
