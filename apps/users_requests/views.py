from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsCustomer, IsStaff
from .models import PartRequestModel
from .serializers import PartRequestSerializer
from rest_framework.pagination import PageNumberPagination
from core.pagination import PagePagination
from ..users.serializers import UserSerializer


class ListCreatePartRequestView(ListAPIView):
     queryset = PartRequestModel.objects.all().order_by('-id')
     permission_classes = (IsStaff,)
     serializer_class = PartRequestSerializer
     pagination_class = PagePagination

class CreatePartRequestView(GenericAPIView):
     permission_classes = (AllowAny,)
     def post(self, *args, **kwargs):
          data = self.request.data
          serializer = PartRequestSerializer(data=data)
          serializer.is_valid(raise_exception=True)
          if self.request.user.is_authenticated:
               user = self.request.user
               serializer.save(user=user)
          else:
               serializer.save()
          return Response(serializer.data, status.HTTP_200_OK)

# class DestroyParRequestView(DestroyAPIView):
#      permission_classes = (AllowAny,)
#      queryset = PartRequestModel.objects.all()
#      serializer_class = PartRequestSerializer

class RequestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     permission_classes = (AllowAny,)
     queryset = PartRequestModel.objects.all()
     serializer_class = PartRequestSerializer




