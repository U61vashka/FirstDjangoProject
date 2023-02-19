from django.core.exceptions import PermissionDenied


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
