from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from core.enums.bad_words import BAD_WORDS
from core.permissions import IsStaff, CanMakeRequest, IsPremium
from .models import PartRequestModel, CheckModel
from .serializers import PartRequestSerializer, RequestPhotoSerializer
from core.pagination import PagePagination
from django.db.models import Avg
from profanityfilter import ProfanityFilter
from django.shortcuts import get_object_or_404
from core.services.currency_service import update_currency_rates
from ..users.models import UserModel
from core.services.email_service import EmailService
pf:ProfanityFilter = ProfanityFilter(extra_censor_list=BAD_WORDS)



class AddPhotoView(UpdateAPIView):
     permission_classes = (IsAuthenticated,)
     serializer_class = RequestPhotoSerializer
     http_method_names = ('put',)
     def get_object(self):
          pk = self.kwargs.get('pk')
          return get_object_or_404(PartRequestModel, pk=pk, user=self.request.user)

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
          volume = request.GET.get('eng_vol')
          year = request.GET.get('year')
          fuel = request.GET.get('fuel')
          region = request.GET.get('region')
          if brand and model and volume and year and fuel:
               try:
                    if not region:
                         average_price = PartRequestModel.objects.filter(car_brand=brand, car_model=model, year=year, engine_volume=volume, fuel=fuel).aggregate(avg_price=Avg('price'))
                    else:
                         average_price = PartRequestModel.objects.filter(car_brand=brand, car_model=model, region_of_car=region).aggregate(avg_price=Avg('price'))
                    return Response({"average_price" : int(average_price['avg_price'])}, status.HTTP_200_OK )
               except Exception as err:
                    return Response({"details" : "Incorrect params"}, status.HTTP_400_BAD_REQUEST)
          else:
               return Response("No params", status.HTTP_400_BAD_REQUEST)

class CreatePartRequestView(CreateAPIView):
     permission_classes = (IsAuthenticated, CanMakeRequest,)
     serializer_class = PartRequestSerializer
     update_currency_rates()


class UpdatePartRequestView(UpdateAPIView):
     permission_classes = (IsAuthenticated, CanMakeRequest,)
     serializer_class = PartRequestSerializer
     queryset = PartRequestModel.objects.all()
     update_currency_rates()
     

     def patch(self, request, *args, **kwargs):
          notice = self.get_object()
          notice.is_active = False
          notice.save()
          return super().patch(request, *args, **kwargs)




class ActivatePartRequestView(GenericAPIView): #id notice
     serializer_class = PartRequestSerializer
     queryset = PartRequestModel.objects.exclude(is_active=True)

     def post(self, *args, **kwargs):
          notice = self.get_object()
          check = CheckModel.objects.filter(notice=notice).first()
          validate = pf.is_clean(notice.about)

          if  validate:
               notice.is_active = True
               notice.save()
               return Response(PartRequestSerializer(notice).data, status=status.HTTP_200_OK)
     
          if check and check.checker:
               count = check.checker +1
          
               if check.checker < 3:
                    setattr(check, "checker", count)
                    check.save()
                    print('now')
               else:
                    EmailService.validate(id=notice.id)
                    return Response({"detail": f"email send"}, status=status.HTTP_200_OK)
          else:
               check = CheckModel.objects.create(notice=notice, checker=1)
          return Response({"detail": f"your fields about not valid try {check.checker}"}, status=status.HTTP_400_BAD_REQUEST)


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




