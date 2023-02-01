from rest_framework import permissions


# https://www.django-rest-framework.org/api-guide/permissions/#examples
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # HEAD is a request method supported by HTTP used by the World Wide Web.
        # The HEAD method asks for a response identical to that of a GET request,
        # but without the response body.

        # The HTTP OPTIONS method is used to request information about the
        # communication options available for the target resource. The response
        # may include an Allow header indicating allowed HTTP methods on the
        # resource, or various Cross Origin Resource Sharing headers.

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner is None:
            return True

        # WARNING Make sure obj.owner matches the model field you want. May be author,
        # creator, etc. depending on resource you are using. If model field differs
        # then update class name as well.
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
