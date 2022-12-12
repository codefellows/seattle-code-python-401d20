from rest_framework import generics
from .serializers import ThingSerializer
from .models import Thing


class ThingList(generics.ListCreateAPIView):

    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


# The ThingDetail needs the same things
class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
