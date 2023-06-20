from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=50)
    alert_email = models.CharField(max_length=50)
    cc_transaction_email_parser = models.CharField(max_length=50)

    def __str__(self):
        return self.name
