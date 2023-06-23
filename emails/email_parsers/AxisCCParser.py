import re
from django.db.models import QuerySet

from cards.models import Card
from emails.email_parsers.BaseEmailParser import BaseEmailParser
from transactions.models import Transaction


class AxisCCParser(BaseEmailParser):

    def __init__(self, email: str, cards: QuerySet(Card), transaction: Transaction):
        if 'Transaction alert on Axis Bank Credit Card no. ' not in email:
            return

        result = re.findall("Card\sno\.\s(.+?)\sfor\sINR\s(.+?)\sat\s(.+?)\son", email)
        print(result)
        card_number = result[0][0]
        while ' ' in card_number:
            card_number = re.findall('Card\sno\.\s(.+?)$', card_number)[0]
        card_number = card_number.replace('X', '')

        amount = int(float(result[0][1]) * 100)
        merchant = result[0][2]

        transaction.card = cards.filter(card_number__endswith=card_number).first()
        transaction.amount_in_paise = amount
        transaction.merchant = merchant

        super().__init__(transaction)
