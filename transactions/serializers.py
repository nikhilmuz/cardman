from rest_framework import serializers

# from cards.models import Card
from transactions.models import *


class CardTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "amount_in_paise", "time", "merchant", "transaction_type", ]


class AllTransactionSerializer(serializers.ModelSerializer):
    card_number = serializers.SerializerMethodField()
    card_bank = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = "__all__"

    @staticmethod
    def get_card_number(obj):
        return obj.card.card_number

    @staticmethod
    def get_card_bank(obj):
        return obj.card.bank.name


class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    # def validate_card(self, value):
    #     if not Card.objects.filter(id=value, user=self.context["request"].user).exists():
    #         raise serializers.ValidationError("Card does not exist")
    #     return value
