from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.request import Request


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
class IsAuthenticatedOrWriteOnly(BasePermission):
    def has_permission(self, request:Request, view):
        if request.method == 'POST':
            return True
        return bool(request.user)

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_seller)
class IsPremium(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_premium)

class CanMakeRequest(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.requests_count < 1 or request.user.is_premium)

