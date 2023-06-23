from transactions.models import Transaction


class BaseEmailParser:

    def __init__(self, transaction: Transaction):
        transaction.save()
