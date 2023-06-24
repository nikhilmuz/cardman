import re
from django.db.models import QuerySet

from cards.models import Card
from emails.email_parsers.BaseEmailParser import BaseEmailParser
from transactions.models import Transaction


class HsbcCCParser(BaseEmailParser):

    def __init__(self, email: str, cards: QuerySet(Card), transaction: Transaction):
        if 'You have used your HSBC Credit Card ending with' not in email:
            return

        result = re.findall("Credit\scard.*with\s(.+?),.*INR\s(.+?)\s.*payment\sto\s(.+?)\s", email)
        card_number = result[0][0]
        amount = int(float(result[0][1].replace(',', '')) * 100)
        merchant = result[0][2]

        transaction.card = cards.filter(card_number__endswith=card_number).first()
        transaction.amount_in_paise = amount
        transaction.merchant = merchant

        super().__init__(transaction)
