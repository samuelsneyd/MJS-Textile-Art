from django.urls import path
from .views import IndexView, AboutView, GalleryView, ResumeView, LinksView, ClassesView

app_name = "quilts"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("about/", AboutView.as_view(), name="about"),
    path("resume/", ResumeView.as_view(), name="resume"),
    path("links/", LinksView.as_view(), name="links"),
    path("classes/", ClassesView.as_view(), name="classes"),
]
