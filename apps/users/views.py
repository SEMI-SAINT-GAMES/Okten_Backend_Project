from rest_framework import status
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     GenericAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer, ProfileAvatarSerializer
from core.dataclasses.user_dataclass import UserDataClass
from core.permissions import IsSuperUser
from datetime import timedelta
from django.utils import timezone


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class GetUsersView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        me = self.request.user
        queryset = UserModel.objects.exclude(id=me.id)
        return queryset

class UserAddAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return UserModel.objects.get(pk=self.request.user.pk).profile

    def perform_update(self, serializer):
        self.get_object().avatar.delete()
        super().perform_update(serializer)


class MakeUserAdminView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)
    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
class MakeAdminUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)
    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)



class UserUnblockView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)
    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
class UserBlockView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)
    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

class UserGetPremiumMounth(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        current_time = timezone.now()
        time_till = current_time + timedelta(days=30)
        if not user.premium_till or current_time > user.premium_till:
            user.premium_till = time_till
            user.save()
        else:
            return Response({"details":"This user is already premium"})
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
class UserGetPremiumYear(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        current_time = timezone.now()
        time_till = current_time + timedelta(days=365)
        if not user.premium_till or current_time > user.premium_till:
            user.premium_till = time_till
            user.save()
        else:
            return Response({"details":"This user is already premium"})
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

class UserBreakPremiumView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        current_time = timezone.now()
        if user.premium_till and current_time < user.premium_till:
            user.premium_till = None
            user.save()
        else:
            return Response({"details":"This user is not premium"})
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)