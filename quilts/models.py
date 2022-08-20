from django.db import models
from django.utils.translation import gettext_lazy as _


class Quilt(models.Model):
    """Quilts displayed in the gallery."""

    class Type(models.TextChoices):
        LARGE_WORKS = "LARGE_WORKS", _("Large Works")
        SMALL_WORKS = "SMALL_WORKS", _("Small Works")
        PORTRAITS = "PORTRAITS", _("Portraits")
        PEOPLE = "PEOPLE", _("People")
        NUDES = "NUDES", _("Nudes")

    class Status(models.TextChoices):
        FOR_SALE = "FOR_SALE", _("For Sale")
        NOT_FOR_SALE = "NOT_FOR_SALE", _("Not for Sale")
        PRIVATE_COLLECTION = "PRIVATE_COLLECTION", _("In a Private Collection")
        TOURING_EXHIBITION = "TOURING_EXHIBITION", _("In a Touring Exhibition")

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    type = models.CharField(max_length=24, choices=Type.choices)
    status = models.CharField(max_length=24, choices=Status.choices)
    # image = models.ImageField(upload_to=MEDIA_URL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
