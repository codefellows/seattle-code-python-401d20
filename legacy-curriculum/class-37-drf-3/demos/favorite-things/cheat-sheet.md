- `$ pipenv install django djangorestframework`
- `$ django-admin startproject favorite_things_project .`
- `$ python manage.py migrate`
- `$ python manage.py createsuperuser`
- `$ python manage.py startapp things`
- add things app to `INSTALLED_APPS`
- add Thing model
- make migrations
- migrate
- add Thing model to admin.py
- add Thing in admin panel
- create `things/serializers.py`
    - create ThingSerializer
- add view
- update `favorite_things_project/urls.py`
- add `things/urls.py`




## Permissions
Open for everybody, NOT cool

- create a new user
- switching users a minor pain
- add `path('api-auth/', include('rest_framework.urls'))` to project urls
- locking down
    - add permissions to things/views
- log out then try api routes
- log in and try again
- Permissions
    - AllowAny
    - IsAuthenticated
    - IsAdminUser
    - IsAuthenticatedOrReadOnly
- Project level permissions
    - ```
    REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': 'rest_framework.permissions.IsAuthenticated'
}
```


- Custom permissions - things/permissions.py
```
from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user
```