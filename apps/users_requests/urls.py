from django.urls import include, path

from .views import (RequestRetrieveUpdateDestroyAPIView,
                    ListCreatePartRequestView,
                    CreatePartRequestView,
                    ListAveragePrice,
                    AddPhotoView)

urlpatterns = [
    path('', ListCreatePartRequestView.as_view(), name='ListCreatePartRequestView'),
    path('/<int:pk>', RequestRetrieveUpdateDestroyAPIView.as_view()),
    path('/create', CreatePartRequestView.as_view()),
    path('/add_photo/<int:pk>', AddPhotoView.as_view()),
    path('/average_price', ListAveragePrice.as_view())
]