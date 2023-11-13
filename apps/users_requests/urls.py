from django.urls import include, path

from .views import (RequestRetrieveUpdateDestroyAPIView,
                    ListCreatePartRequestView,
                    CreatePartRequestView,
                    ListAveragePrice,
                    AddPhotoView,
                    ActivatePartRequestView, UpdatePartRequestView)

urlpatterns = [
    path('', ListCreatePartRequestView.as_view(), name='ListCreatePartRequestView'),
    path('/<int:pk>', RequestRetrieveUpdateDestroyAPIView.as_view(), name='get_by_id'),
    path('/create', CreatePartRequestView.as_view(), name='create'),
    path('/update', UpdatePartRequestView.as_view(), name='update'),
    path('/add_photo/<int:pk>', AddPhotoView.as_view(), name='add_photo'),
    path('/average_price', ListAveragePrice.as_view(), name='average_price'),
    path('/activate/<int:pk>', ActivatePartRequestView.as_view(), name='activate_request')
]