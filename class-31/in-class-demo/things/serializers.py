# Imports the serializers module from the djangorestframework library. This module provides a set of classes for converting complex data types, such as Django models, into Python data types that can be easily rendered into JSON or other content types.
from rest_framework import serializers
# Imports the Thing model from the same directory as the current file. This is the model that we will be serializing.
from .models import Thing


# Defines a new class, ThingSerializer, which subclasses serializers.ModelSerializer. This means that the ThingSerializer class inherits all the behavior of serializers.ModelSerializer, but can also add or override behavior as needed.
class ThingSerializer(serializers.ModelSerializer):
    # Defines an inner class, Meta, which is used to specify metadata about the serializer class.
    class Meta:
        # Specifies the fields from the Thing model that should be included in the serialized representation.
        fields = ('id', 'owner', 'name', 'description', 'created_at')
        # Specifies the model that the serializer should use to generate the serialized representation. This is the Thing model that we imported earlier.
        model = Thing
