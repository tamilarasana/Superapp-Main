from django.db import models


class RTO(models.Model):
    DISPLAY_ORDER = models.CharField(max_length=255, blank=True, null=True)
    IS_POPULAR = models.CharField(max_length=255, blank=True, null=True)
    RTO_CODE = models.CharField(max_length=255, blank=True, null=True)
    RTO_ID = models.CharField(max_length=255, blank=True, null=True)
    RTO_NAME = models.CharField(max_length=255, blank=True, null=True)


class City(models.Model):
    TITLE = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self) -> str:
        return self.TITLE

    class Meta:
        verbose_name = 'OUTLET CITY'
        verbose_name_plural = 'OUTLET CITY'


class Outlet(models.Model):
    CITY = models.ForeignKey(
        City, on_delete=models.CASCADE, blank=True, null=True, related_name='city')
    NAME = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'OUTLET LOCATION'
        verbose_name_plural = 'OUTLET LOCATION'


class PaymentMode(models.Model):
    ACTIVE = 'Active'
    INACTIVE = 'InActive'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'InActive'),
    ]
    PAYMENT_MODE_NAME = models.CharField(max_length=250, blank=True, null=True)
    STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        verbose_name = 'PAYMENT MODE'
        verbose_name_plural = 'PAYMENT MODE'


class AppVersion(models.Model):
    VERSION_NAME = models.CharField(max_length=250, blank=True, null=True)
    VERSION_DESCRIPTION = models.CharField(
        max_length=250, blank=True, null=True)
    VERSION_NUMBER = models.CharField(max_length=250, blank=True, null=True)
    VERSION_NOTES = models.CharField(max_length=250, blank=True, null=True)
    VERSION_REMARKS = models.CharField(max_length=250, blank=True, null=True)
    VERSION_STATUS = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'APP VERSIONS'
        verbose_name_plural = 'APP VERSIONS'
