from django.urls import path
from apps.autoparks.views import AutoparkListCreateView, AutoParkAddCarView, AutoParkRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('', AutoparkListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='park_add_car'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyAPIView.as_view(), name='park_by_id')
]