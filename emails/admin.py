from django.contrib import admin
from django import forms
from emails import models


class EmailAdmin(admin.ModelAdmin):
    """Settings for the Email class in Django admin."""

    readonly_fields = ("created_at", "updated_at", "id")

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {"message": forms.Textarea}
        return super().get_form(request, obj, **kwargs)


admin.site.register(models.Email, EmailAdmin)
