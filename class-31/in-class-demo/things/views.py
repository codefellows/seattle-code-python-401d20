from rest_framework import generics
from .serializers import ThingSerializer
from .models import Thing


class ThingList(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
