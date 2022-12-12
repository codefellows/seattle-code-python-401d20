from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=256)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name