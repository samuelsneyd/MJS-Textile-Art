from rest_framework import serializers
from emails import models


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = "__all__"
