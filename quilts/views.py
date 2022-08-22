from django.views.generic import TemplateView, ListView
from .models import Quilt


class IndexView(TemplateView):
    template_name = "quilts/index.html"


class GalleryView(ListView):
    model = Quilt
    context_object_name = "quilts"
    template_name = "quilts/gallery.html"

    def get_queryset(self):
        query_type = self.request.GET.get("type")
        query_status = self.request.GET.get("status")

        if query_type is not None and query_status is not None:
            return Quilt.objects.filter(type=query_type, status=query_status)

        if query_type is not None:
            return Quilt.objects.filter(type=query_type)

        if query_status is not None:
            return Quilt.objects.filter(status=query_status)

        return Quilt.objects.all()


class AboutView(TemplateView):
    template_name = "quilts/about.html"


class ResumeView(TemplateView):
    template_name = "quilts/resume.html"


class LinksView(TemplateView):
    template_name = "quilts/links.html"


class ClassesView(TemplateView):
    template_name = "quilts/classes.html"


class ContactView(TemplateView):
    template_name = "quilts/contact.html"
