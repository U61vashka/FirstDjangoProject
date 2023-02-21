from django.core.exceptions import PermissionDenied
from rest_framework import permissions
from rest_framework.permissions import BasePermission


class MustBeAuthorMixin(object):

    def has_permissions(self):
        if (self.get_object().creator == None):
            return True
        return self.get_object().creator == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise PermissionDenied('You do not have permission.')
        return super(MustBeAuthorMixin, self).dispatch(
            request, *args, **kwargs)


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user
