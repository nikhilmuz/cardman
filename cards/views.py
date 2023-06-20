from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *


class CardListView(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return Card.objects.filter(user=user)

    serializer_class = CardSerializer


class CardAddView(CreateAPIView):
    serializer_class = CardAddSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
