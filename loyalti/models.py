from django.db import models
from profileutility.models import *
from showcase.models import *

class Loyalti(models.Model):
    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    TOTAL_EARNED_POINTS = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0) 
    BALANCE_POINTS = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    LAST_UPDATED_POINTS = models.DateTimeField(auto_now=True)
    BUSINESS_TURNOVER = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'LOYALTY SUMMARY'
        verbose_name_plural = 'LOYALTY SUMMARY'


class LoyaltiTransaction(models.Model):
    SUCCESS = 'Success'
    FAILED = 'Failed'

    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (FAILED, 'Failed'),
    ]

    ADD = 'Add'
    REDEEM = 'Redeem'

    TRANSACTION_CHOICES = [
        (ADD, 'Add'),
        (REDEEM, 'Redeem'),
    ]

    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    LOYALTI = models.ForeignKey(
        Loyalti, on_delete=models.CASCADE, blank=True, null=True)
    AMOUNT = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=None)
    TIME_OF_TRANSACTION = models.DateTimeField(auto_now=True)
    TRANSACTION_TYPE = models.CharField(
        max_length=50, choices=TRANSACTION_CHOICES, default=None)

    class Meta:
        verbose_name = 'LOYALTY TRANSACTIONS'
        verbose_name_plural = 'LOYALTY TRANSACTIONS'


class LoyaltiEntity(models.Model):
    MEMBER = 'Member'
    GOLD = 'Gold'
    PLATINUM = 'Platinum'

    CATEGORY_CHOICES = [
        (MEMBER, 'Member'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
    ]

    CATEGORY = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default=MEMBER)
    POINTS_ADD_PER_100 = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    POINTS_UPGRADE = models.IntegerField(default=0, blank=True, null=True)
    TIME_OF_UPDATE = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'LOYALTY CLAUSE'
        verbose_name_plural = 'LOYALTY CLAUSE'

