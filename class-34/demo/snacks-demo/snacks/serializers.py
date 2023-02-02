from rest_framework import serializers
from .models import Snack


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = "__all__"
