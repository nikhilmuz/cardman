from collections import OrderedDict

from rest_framework.generics import ListAPIView, CreateAPIView

from cards.models import Card
from transactions.serializers import *


class CardTransactionListView(ListAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(card=Card.objects.get(id=self.kwargs["card_id"], user=self.request.user))
    serializer_class = CardTransactionSerializer


class AllTransactionListView(ListAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(card__in=Card.objects.filter(user=self.request.user))
    serializer_class = AllTransactionSerializer


class AddTransactionView(CreateAPIView):
    serializer_class = AddTransactionSerializer

    def perform_create(self, serializer):
        serializer.save(card=Card.objects.get(id=self.request.data["card"], user=self.request.user))
