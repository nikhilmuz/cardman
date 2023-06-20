from django.contrib.auth.models import User
from banks.models import Bank


class BaseEmailParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(email: str, user: User, bank: Bank):
        raise NotImplementedError("You must implement parse() method in your parser class")
