from rest_framework import generics
from .models import Thing
from .serializers import ThingSerializer
from .permissions import IsCreatorOrReadOnly

class ThingList(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly, )
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
