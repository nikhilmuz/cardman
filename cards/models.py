from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model

from cardman import settings


class Card(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bank = models.ForeignKey('banks.Bank', on_delete=models.CASCADE)

    def get_balance(self):
        cr_sum = self.transaction_set.filter(transaction_type='CR').aggregate(Sum('amount_in_paise'))[
                     'amount_in_paise__sum'] or 0
        dr_sum = self.transaction_set.filter(transaction_type='DR').aggregate(Sum('amount_in_paise'))[
                     'amount_in_paise__sum'] or 0
        return (cr_sum - dr_sum) / 100

    def __str__(self):
        return "{0} ({1})".format(self.card_number, self.bank.name)
