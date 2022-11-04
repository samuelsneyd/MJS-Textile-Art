from django.views.generic import TemplateView, ListView
from .models import Quilt


class IndexView(TemplateView):
    template_name = "quilts/index.html"


class GalleryView(ListView):
    model = Quilt
    context_object_name = "quilts"
    template_name = "quilts/gallery.html"

    def get_queryset(self):
        try:
            query_types = self.request.GET.get("type").upper().split(" ")
        except AttributeError:
            query_types = None

        try:
            query_statuses = self.request.GET.get("status").upper().split(" ")
        except AttributeError:
            query_statuses = None

        if query_types is not None and query_statuses is not None:
            return Quilt.objects.filter(type__in=query_types, status__in=query_statuses)

        if query_types is not None:
            return Quilt.objects.filter(type__in=query_types)

        if query_statuses is not None:
            return Quilt.objects.filter(status__in=query_statuses)

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
