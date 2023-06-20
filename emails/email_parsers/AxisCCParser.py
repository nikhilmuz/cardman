import re

from cards.models import Card
from emails.email_parsers.BaseEmailParser import BaseEmailParser
from transactions.models import Transaction


class AxisCCParser(BaseEmailParser):

    def __init__(self):
        super().__init__()

    @staticmethod
    def parse(email, user, bank):
        if 'Transaction alert on Axis Bank Credit Card no. ' not in email:
            return

        result = re.findall("Card\sno\.\s(.+?)\sfor\sINR\s(.+?)\sat\s(.+?)\son", email)
        card_number = result[0][0]
        while ' ' in card_number:
            card_number = re.findall('Card\sno\.\s(.+?)$', card_number)[0]
        card_number = card_number.replace('X', '')

        amount = int(float(result[0][1]) * 100)
        store = result[0][2]

        card = Card.objects.get(card_number__endswith=card_number, bank=bank, user=user)
        Transaction.objects.create(card=card, amount_in_paise=amount, merchant=store)
