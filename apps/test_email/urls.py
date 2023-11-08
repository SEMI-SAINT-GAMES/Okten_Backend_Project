from django.urls import path

from apps.test_email.views import TestEmailView

urlpatterns = {
    path('', TestEmailView.as_view())
}