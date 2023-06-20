from rest_framework import serializers

from cards.models import *


class CardSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    bank_name = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ["id", "card_number", "bank_name", "balance"]

    def get_balance(self, obj):
        return obj.get_balance()

    def get_bank_name(self, obj):
        return obj.bank.name


class CardAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ["user", ]
