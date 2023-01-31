from django.contrib.auth import get_user_model
from django.db import models


class Thing(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()

    # DateTimeField

    # DateField.auto_now_add: Automatically set the field to now when the object is first created.
    # Useful for creation of timestamps.

    # The default time zone is the time zone defined by the TIME_ZONE setting.

    created_at = models.DateTimeField(auto_now_add=True)

    # DateField.auto_now: Automatically set the field to now every time the
    # object is saved. Useful for “last-modified” timestamps.
    # !! The options auto_now_add, auto_now, and default are mutually
    # exclusive.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
