from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Thing(models.Model):
    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image_url = models.URLField(default="https://http.cat/404")
    reference_url = models.URLField(default="https://http.cat/404")
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('thing_detail', args=[str(self.id)])
