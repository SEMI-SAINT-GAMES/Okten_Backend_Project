from django_filters.rest_framework import DjangoFilterBackend as filters, DjangoFilterBackend

from core.permissions import IsSuperUser, IsStaff
from .models import CarModel
from .filters import CarFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CarSerializer, CarAvatarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    pagination_class = PageNumberPagination
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarsInAutopark(ListAPIView):
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        autopark_id = self.kwargs.get('pk', 1)
        print(autopark_id)
        queryset = CarModel.objects.all().filter(autopark_id=autopark_id)
        return queryset



class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

class CarAddAvatarView(UpdateAPIView):
    permission_classes = (IsStaff,)
    queryset = CarModel.objects.all()
    serializer_class = CarAvatarSerializer
    http_method_names = ('put',)
    #
    # def get_object(self):
    #     return CarModel.objects.get(pk=self.request.car.pk).profile
    #
    def perform_update(self, serializer):
        self.get_object().avatar.delete()
        super().perform_update(serializer)