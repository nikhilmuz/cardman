import re

from cards.models import Card
from emails.email_parsers.BaseEmailParser import BaseEmailParser
from transactions.models import Transaction


class IndusindCCParser(BaseEmailParser):

    def __init__(self):
        super().__init__()

    @staticmethod
    def parse(email, user, bank):
        if 'Transaction Alert - IndusInd Bank Credit Card' not in email:
            return

        result = re.findall("Card\sending\s(.+?)\sfor\sINR\s(.+?)\son\s(.+?)\sat\s(.+?)\sis\s(.+?)\.", email)
        card_number = result[0][0]
        amount = int(float(result[0][1].replace(',', '')) * 100)
        store = result[0][3]
        is_approved = result[0][4] == 'Approved'

        if (is_approved is False):
            print("Transaction For Indusind Credit Card {} for amount was not approved".format(card_number, amount))
            return

        card = Card.objects.get(card_number__endswith=card_number, bank=bank, user=user)
        Transaction.objects.create(card=card, amount_in_paise=amount, merchant=store)
