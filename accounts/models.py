from django.db import models


# Create your models here.


class Account(models.Model):
    account_name = models.CharField(max_length=30)
    usd_total_value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.account_name


class Asset(models.Model):
    asset_name = models.CharField(max_length=30)
    usd_value = models.FloatField()

    def __str__(self):
        return self.asset_name


class Balance(models.Model):
    quantity = models.PositiveIntegerField()
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE)
