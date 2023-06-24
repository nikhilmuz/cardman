import re

from cards.models import Card
from emails.email_parsers.BaseEmailParser import BaseEmailParser
from transactions.models import Transaction


class HdfcCCParser(BaseEmailParser):

    def __init__(self):
        super().__init__()

    @staticmethod
    def parse(email, user, bank):
        if 'Alert : Update on your HDFC Bank Credit Card' not in email:
            return

        result = re.findall("Card\sending\s(.+?)\sfor\sRs\s(.+?)\sat\s(.+?)\son", email)
        card_number = result[0][0]
        amount = int(float(result[0][1].replace(',', '')) * 100)
        store = result[0][3]

        card = Card.objects.get(card_number__endswith=card_number, bank=bank, user=user)
        Transaction.objects.create(card=card, amount_in_paise=amount, merchant=store)
