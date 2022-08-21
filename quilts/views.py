from django.views.generic.base import TemplateView
from .models import Quilt


class IndexView(TemplateView):
    template_name = "quilts/index.html"


class GalleryView(TemplateView):
    template_name = "quilts/gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quilts"] = Quilt.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "quilts/about.html"


class ResumeView(TemplateView):
    template_name = "quilts/resume.html"


class LinksView(TemplateView):
    template_name = "quilts/links.html"


class ClassesView(TemplateView):
    template_name = "quilts/classes.html"
