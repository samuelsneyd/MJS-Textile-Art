from django.urls import path
from .views import EmailView

app_name = "emails"

urlpatterns = [
    path("email", EmailView.as_view(), name="emails"),
]
