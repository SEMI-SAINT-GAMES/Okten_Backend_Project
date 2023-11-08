from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.services.email_service import EmailService


class TestEmailView(GenericAPIView):
    def get(self, *args, **kwargs):
        EmailService.test_email()
        return Response('ok')
