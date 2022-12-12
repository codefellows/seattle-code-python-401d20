### Typical Django flow
- `$ django_admin startproject things_project .`
- `$ python manage.py migrate`
- `$ python manage.py runserver`

### Running? Great, then proceed
- open `http://localhost:8000/admin` in browser
- hmm, no user. Let's create one, a `super` one at that
- `$ python manange.py createsuperuser` and follow prompts
- Now go to `http://localhost:8000/admin` and log in
- Bask in glory


### Users and Groups you get for free. Let's make a Model of our own
- `$ python manage.py startapp things`
- Update `things_project/settings.py` at bottom of `INSTALLED_APPS` section with `'things.apps.ThingsConfig',`
    - Don't forget comma on the previous final line
- Now create a `Thing` model in `things/models.py`
```
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=256)
```
- `$ python manage.py makemigrations things`
- `$ python manage.py migrate`
- To add to admin panel we need one more thing to `things/admin.py`
- Add `from .models import Thing` and `admin.site.register(Thing)`
- go to `http://localhost:8000/admin` and log in
- Bask in glory some more