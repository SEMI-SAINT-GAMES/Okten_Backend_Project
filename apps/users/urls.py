from django.urls import path
from .views import UserCreateView, GetUsersView, UserAddAvatarView, MakeUserAdminView, MakeAdminUserView, UserBlockView, \
    UserUnblockView

urlpatterns = [
    path('', UserCreateView.as_view(), name='users_create'),
    path('/all', GetUsersView.as_view()),
    path('/avatars', UserAddAvatarView.as_view(), name='users_add_avatar'),
    path('/<int:pk>/user_to_admin', MakeUserAdminView.as_view()),
    path('/<int:pk>/admin_to_user', MakeAdminUserView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnblockView.as_view())
]