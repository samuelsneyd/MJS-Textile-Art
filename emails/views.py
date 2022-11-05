from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from emails.models import Email
from emails.serializers import EmailSerializer


class EmailView(APIView):
    """An API View for creating emails."""

    bad_request_message = {"message": "bad request"}
    subject = "Inquiry about MJS Textile Art"

    def post(self, request) -> Response:
        """Creates and sends an email."""

        data = request.data
        data["sender"] = data["email"]
        data["recipient"] = settings.RECIPIENT_EMAIL
        data["subject"] = f'{self.subject}: {data["name"]}'

        serializer = EmailSerializer(data=data)

        if serializer.is_valid():
            email: Email = serializer.save()
            email.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(self.bad_request_message, status=status.HTTP_400_BAD_REQUEST)
