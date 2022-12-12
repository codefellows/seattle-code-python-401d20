from rest_framework import generics
from .models import Thing
from .permissions import IsOwnerOrReadOnly
from .serializers import ThingSerializer


class ThingList(generics.ListCreateAPIView):

    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


# The ThingDetail needs the same things
class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
