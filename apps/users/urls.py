from django.urls import path
from .views import (UserCreateView,
                    GetUsersView,
                    UserAddAvatarView,
                    MakeUserAdminView,
                    MakeAdminUserView,
                    UserBlockView,
                    UserUnblockView,
                    UserGetPremiumMounth,
                    UserGetPremiumYear,
                    UserBreakPremiumView)

urlpatterns = [
    path('', UserCreateView.as_view(), name='users_create'),
    path('/all', GetUsersView.as_view(), name='get_all_users_except_me'),
    path('/avatars', UserAddAvatarView.as_view(), name='users_add_avatar'),
    path('/<int:pk>/user_to_admin', MakeUserAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/admin_to_user', MakeAdminUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='block'),
    path('/<int:pk>/unblock', UserUnblockView.as_view(), name='unblock'),
    path('/<int:pk>/get_premium_on_mounth', UserGetPremiumMounth.as_view(), name='get_premium_on_mounth'),
    path('/<int:pk>/get_premium_on_year', UserGetPremiumYear.as_view(), name='get_premium_on_year'),
    path('/<int:pk>/break_premium', UserBreakPremiumView.as_view(), name='break_premium')
]