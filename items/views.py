from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Item
from .serializers import ItemSerializer

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Item.objects.get(id=self.kwargs['pk'])
        except Item.DoesNotExist:
            raise NotFound()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
