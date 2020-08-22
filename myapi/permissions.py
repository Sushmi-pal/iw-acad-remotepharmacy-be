from rest_framework.permissions import BasePermission
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

# class IsLoggedInUser(BasePermission):
#     user_token = Token.objects.get(key='token string').user
#     def has_permission(self,request,view):
#         if user:
#             return request.user.is_authenticated