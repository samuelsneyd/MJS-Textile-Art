from django.contrib import admin
from django import forms
from quilts import models


class QuiltAdmin(admin.ModelAdmin):
    """Settings for the Quilt class in Django admin"""

    readonly_fields = ("created_at", "updated_at", "id")

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {"description": forms.Textarea}
        return super().get_form(request, obj, **kwargs)


admin.site.register(models.Quilt, QuiltAdmin)
