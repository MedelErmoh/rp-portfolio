from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("projects/", include("projects.urls")),
    path("projects/", include('django.contrib.auth.urls')),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]