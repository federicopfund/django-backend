from django.contrib import admin
from django.urls import path, include  # import new funtion from django.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),  # new app
]
