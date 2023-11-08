from django.urls import include, path

from .views import RequestRetrieveUpdateDestroyAPIView, ListCreatePartRequestView, CreatePartRequestView

urlpatterns = [
    path('', ListCreatePartRequestView.as_view(), name='ListCreatePartRequestView'),
    path('/<int:pk>', RequestRetrieveUpdateDestroyAPIView.as_view()),
    path('/create', CreatePartRequestView.as_view()),
]