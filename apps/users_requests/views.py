from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsStaff, CanMakeRequest, IsPremium
from .models import PartRequestModel
from .serializers import PartRequestSerializer
from rest_framework.pagination import PageNumberPagination
from core.pagination import PagePagination
from ..users.serializers import UserSerializer
from django.db.models import Avg





class ListCreatePartRequestView(ListAPIView):
     queryset = PartRequestModel.objects.all().order_by('-id')
     permission_classes = (IsStaff,)
     serializer_class = PartRequestSerializer
     pagination_class = PagePagination

class ListAveragePrice(GenericAPIView):
     permission_classes = (IsPremium,)
     def get(self, request, *args, **kwargs):
          brand = request.GET.get('brand')
          model = request.GET.get('model')
          if brand and model:
               try:
                    average_price = PartRequestModel.objects.filter(car_brand=brand, car_model=model).aggregate(avg_price=Avg('price'))
                    #if (average_price):
                    return Response({"average_price" : int(average_price['avg_price'])}, status.HTTP_200_OK )
               except Exception as err:
                    return Response({"details" : "Incorrect params"}, status.HTTP_400_BAD_REQUEST)
          else:
               return Response("No params", status.HTTP_400_BAD_REQUEST)

class CreatePartRequestView(GenericAPIView):
     permission_classes = (IsAuthenticated, CanMakeRequest,)
     def post(self, *args, **kwargs):
          data = self.request.data
          serializer = PartRequestSerializer(data=data)
          serializer.is_valid(raise_exception=True)
          if self.request.user.is_authenticated:
               user = self.request.user
               user.requests_count += 1
               user.save()
               serializer.save(user=user)

          return Response(serializer.data, status.HTTP_200_OK)

# class DestroyParRequestView(DestroyAPIView):
#      permission_classes = (AllowAny,)
#      queryset = PartRequestModel.objects.all()
#      serializer_class = PartRequestSerializer

class RequestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     permission_classes = (AllowAny,)
     queryset = PartRequestModel.objects.all()
     serializer_class = PartRequestSerializer

     def get(self, request, *args, **kwargs):
          instance = self.get_object()
          instance.view_count += 1
          instance.save(3)

          serializer = self.get_serializer(instance)
          return Response(serializer.data, status=status.HTTP_200_OK)




