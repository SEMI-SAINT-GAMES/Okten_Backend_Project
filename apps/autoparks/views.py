from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, GenericAPIView,  RetrieveUpdateDestroyAPIView
from apps.autoparks.models import AutoParkModel
from apps.autoparks.serializre import AutoParkSerializer
from apps.cars.serializers import CarSerializer
from rest_framework.pagination import PageNumberPagination

from core.permissions import IsStaff


class AutoparkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)



class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsStaff,)
    def post(self, *args, **kwargs):
        autopark = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(autopark=autopark)
        park_serializer = AutoParkSerializer(autopark)
        print('autopart')
        print(type(autopark))
        print("data")
        print(data)


        return Response(park_serializer.data, status.HTTP_200_OK)
class AutoParkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsStaff,)






