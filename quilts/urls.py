from django.urls import path
from .views import (
    IndexView,
    AboutView,
    GalleryView,
    ResumeView,
    LinksView,
    ClassesView,
    ContactView,
    QuiltView,
)

app_name = "quilts"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("gallery/<int:pk>", QuiltView.as_view(), name="quilt"),
    path("gallery/<str:quilt>", QuiltView.as_view(), name="quilt"),
    path("about/", AboutView.as_view(), name="about"),
    path("resume/", ResumeView.as_view(), name="resume"),
    path("links/", LinksView.as_view(), name="links"),
    path("classes/", ClassesView.as_view(), name="classes"),
    path("contact/", ContactView.as_view(), name="contact"),
]
