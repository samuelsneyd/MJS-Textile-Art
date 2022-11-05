from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Quilt


class IndexView(TemplateView):
    template_name = "quilts/index.html"


class GalleryView(ListView):
    model = Quilt
    paginate_by = 12
    context_object_name = "quilts"
    template_name = "quilts/gallery.html"

    def get_queryset(self):
        try:
            types = self.request.GET.get("type").upper().split(" ")
        except AttributeError:
            types = None

        try:
            statuses = self.request.GET.get("status").upper().split(" ")
        except AttributeError:
            statuses = None

        if types is not None and statuses is not None:
            queryset = Quilt.objects.filter(type__in=types, status__in=statuses)
        elif types is not None:
            queryset = Quilt.objects.filter(type__in=types)
        elif statuses is not None:
            queryset = Quilt.objects.filter(status__in=statuses)
        else:
            queryset = Quilt.objects.all()

        return queryset.order_by("-pk")


class QuiltView(ListView):
    model = Quilt
    context_object_name = "quilt"
    template_name = "quilts/quilt.html"

    def get_queryset(self):
        try:
            title = self.kwargs["quilt"]
            return get_object_or_404(Quilt, title=title)
        except KeyError:
            pk = self.kwargs["pk"]
            return get_object_or_404(Quilt, pk=pk)


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
