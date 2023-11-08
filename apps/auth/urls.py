from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import MeView, ActivateUserView, PasswordRecoveryRequestView, PasswordRecoveryView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/me', MeView.as_view(), name='auth_me'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate_user'),
    path('/recovery/request', PasswordRecoveryRequestView.as_view(), name='recovery_request'),
    path('/recovery/<str:token>', PasswordRecoveryView.as_view(), name='password_recovery')
]