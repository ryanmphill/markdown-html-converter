from django.contrib import admin
from django.urls import include, path
from mdconverterapi import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("markdown-to-html", views.markdown_to_html),
    path("html-to-markdown", views.html_to_markdown),
]
