from django.db import models
from profileutility.models import *
from showcase.models import *


class AppBooking(models.Model):
    SUCCESS = 'Success'
    PENDING = 'Pending'
    ERROR = 'Error'
    DECLINED = 'Declined'

    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (PENDING, 'Pending'),
        (ERROR, 'Error'),
        (DECLINED, 'Declined')
    ]

    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    ITEMLIST = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_DESCRIPTION = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    PAYMENT_STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=PENDING)
    PAYMENT_ID = models.CharField(
        max_length=250, blank=True, null=True)
    AMOUNT = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    CUST_ID_OR_REG_NO = models.CharField(
        max_length=250, blank=True, null=True)

    MODE_OF_PAYMENT = models.CharField(
        max_length=250, blank=True, null=True)
    GATEWAY_SESSION_ID = models.CharField(
        max_length=250, blank=True, null=True)
    GATEWAY_ORDER_ID = models.CharField(
        max_length=250, blank=True, null=True)
    CRMID = models.CharField(
        max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'APEX'
        verbose_name_plural = 'APEX'


class NewCarBooking(models.Model):
    PENDING = 'Pending'
    BOOKED = 'Booked'
    RETAIL = 'Retail'
    RETAILCANCEL = 'RetailCancel'
    DELIVERRED = 'Deliverred'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (BOOKED, 'Booked'),
        (RETAIL, 'Retail'),
        (RETAILCANCEL, 'RetailCancel'),
        (DELIVERRED, 'Deliverred')
    ]
    NAME = models.CharField(max_length=250, blank=True, null=True)
    EMAIL = models.CharField(max_length=250, blank=True, null=True)
    MOBILE = models.CharField(max_length=250, blank=True, null=True)
    CUST_ID_OR_REG_NO = models.CharField(
        max_length=250, blank=True, null=True)

    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    ADDRESS = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_DESCRIPTION = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    BOOKING_ID = models.ForeignKey(
        AppBooking, related_name="bookin_desc_newcar", on_delete=models.CASCADE, blank=True, null=True)

    CITY = models.CharField(max_length=250, blank=True, null=True)
    OUTLETS = models.CharField(max_length=250, blank=True, null=True)
    ITEM_PRICE = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    EMPLOYEE_ID = models.CharField(max_length=255, blank=True, null=True)
    REFERRED_BY = models.CharField(max_length=255, blank=True, null=True)

    BOOKING_STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        verbose_name = 'NEW CAR'
        verbose_name_plural = 'NEW CAR'


class UsedCarBooking(models.Model):

    ENQUIRED = 'Enquired'
    CONTACTED = 'Contacted'
    BOOKED = 'Booked'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'
    CAR_NOT_AVAILABLE = 'Car not available'

    STATUS_CHOICES = [
        (ENQUIRED, 'Enquired'),
        (CONTACTED, 'Contacted'),
        (BOOKED, 'Booked'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled'),
        (CAR_NOT_AVAILABLE, 'Car not available')
    ]

    ITEMLIST = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_DESCRIPTION = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    BOOKING_ID = models.ForeignKey(
        AppBooking, on_delete=models.CASCADE, blank=True, null=True)
    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    ADDRESS = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)

    BRAND = models.CharField(max_length=250, blank=True, null=True)
    MODEL = models.CharField(max_length=250, blank=True, null=True)
    TRANSMISSION = models.CharField(max_length=250, blank=True, null=True)
    FUEL = models.CharField(max_length=250, blank=True, null=True)
    YEAR = models.CharField(max_length=250, blank=True, null=True)
    NAME = models.CharField(max_length=250, blank=True, null=True)
    PHONE = models.CharField(max_length=250, blank=True, null=True)
    EMAIL = models.CharField(max_length=250, blank=True, null=True)
    CUST_ID_OR_REG_NO = models.CharField(
        max_length=250, blank=True, null=True)
    KMS_DRIVEN_STARTING = models.CharField(
        max_length=250, blank=True, null=True)
    KMS_DRIVEN_ENDING = models.CharField(max_length=250, blank=True, null=True)
    PRICE = models.CharField(max_length=250, blank=True, null=True)
    LAT = models.CharField(max_length=250, blank=True, null=True)
    LONG = models.CharField(max_length=250, blank=True, null=True)
    ENQUIRE_AT = models.DateTimeField(auto_now_add=True)
    SCHEDULED = models.DateTimeField(auto_now=True, blank=True, null=True)
    EMPLOYEE_ID = models.CharField(max_length=255, blank=True, null=True)
    REFERRED_BY = models.CharField(max_length=255, blank=True, null=True)

    NUMBER_OF_OWNERS = models.CharField(max_length=50, blank=True, null=True)
    TYPE = models.CharField(max_length=50, blank=True, null=True)

    BOOKING_STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ENQUIRED)

    class Meta:
        verbose_name = 'USED CAR - BUY'
        verbose_name_plural = 'USED CAR - BUY'


class Service(models.Model):

    PENDING = 'Pending'
    BOOKED = 'Booked'
    CONTACTED = 'Contacted'
    PICKED = 'Picked Up'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (BOOKED, 'Booked'),
        (CONTACTED, 'Contacted'),
        (PICKED, 'Picked Up'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled')
    ]

    BOOKING_ID = models.ForeignKey(
        AppBooking, related_name="bookin_desc_service", on_delete=models.CASCADE, blank=True, null=True)
    ITEMLIST = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_DESCRIPTION = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    ADDRESS = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)

    NAME = models.CharField(max_length=255, blank=True, null=True)
    EMAIL = models.CharField(max_length=255, blank=True, null=True)
    MOBILE = models.CharField(max_length=255, blank=True, null=True)
    CUST_ID_OR_REG_NO = models.CharField(
        max_length=250, blank=True, null=True)
    CITY = models.CharField(max_length=255, blank=True, null=True)
    OUTLET = models.CharField(max_length=255, blank=True, null=True)

    MODEL = models.CharField(max_length=255, blank=True, null=True)
    VARIENT = models.CharField(max_length=255, blank=True, null=True)
    COLOR = models.CharField(max_length=255, blank=True, null=True)

    PICKUP_SLOT = models.DateTimeField(auto_now=True)
    ITEM_PRICE = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    EMPLOYEE_ID = models.CharField(max_length=255, blank=True, null=True)
    REFERRED_ID = models.CharField(max_length=255, blank=True, null=True)

    DELIVERRED_TIME = models.DateTimeField(blank=True, null=True)
    BOOKING_STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        verbose_name = 'SERVICE'
        verbose_name_plural = 'SERVICE'


class Accessory(models.Model):

    BOOKED = 'Booked'
    DISPATCHED = 'Booked'
    OUT_FOR_DELIVERY = 'Contacted'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (BOOKED, 'Booked'),
        (DISPATCHED, 'Contacted'),
        (OUT_FOR_DELIVERY, 'Picked Up'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled')
    ]

    BOOKING_ID = models.ForeignKey(
        AppBooking, on_delete=models.CASCADE, blank=True, null=True)
    ITEMLIST = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_DESCRIPTION = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    CUST_ID_OR_REG_NO = models.CharField(
        max_length=250, blank=True, null=True)
    ADDRESS = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_PRICE = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    QUANTITY = models.IntegerField(default=1, blank=True)

    DELIVERRED_TIME = models.DateTimeField(blank=True, null=True)
    BOOKING_STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        verbose_name = 'ACCESSORY'
        verbose_name_plural = 'ACCESSORY'


class Insurance(models.Model):

    ENQUIRED = 'Enquired'
    CONTACTED = 'Contacted'
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (ENQUIRED, 'Enquired'),
        (CONTACTED, 'Contacted'),
        (BOOKED, 'Booked'),
        (CANCELLED, 'Cancelled')
    ]
    ITEMLIST = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_DESCRIPTION = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    PROFILE = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    ADDRESS = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)

    NAME = models.CharField(max_length=255, blank=True, null=True)
    EMAIL = models.CharField(max_length=255, blank=True, null=True)
    MOBILE = models.CharField(max_length=255, blank=True, null=True)

    REGISTERED_NUMBER = models.CharField(max_length=255, blank=True, null=True)
    REGISTERED_CITY = models.CharField(max_length=255, blank=True, null=True)
    MODEL = models.CharField(max_length=255, blank=True, null=True)
    VARIANT = models.CharField(max_length=255, blank=True, null=True)
    FUEL = models.CharField(max_length=255, blank=True, null=True)
    REG_DATE = models.DateTimeField(auto_now=True)
    POLICY_EXPIRE_DATE = models.DateTimeField(auto_now=True)
    LAST_CLAIM_STATUS = models.CharField(max_length=255, blank=True, null=True)
    CLAIM_BONUS = models.CharField(max_length=255, blank=True, null=True)

    EMPLOYEE_ID = models.CharField(max_length=255, blank=True, null=True)
    REFFERED_BY= models.CharField(max_length=255, blank=True, null=True)
    ADDONS = models.CharField(max_length=255, blank=True, null=True)

    BOOKED_AT = models.DateTimeField(blank=True, null=True)
    BOOKING_STATUS = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ENQUIRED)

    class Meta:
        verbose_name = 'INSURANCE'
        verbose_name_plural = 'INSURANCE'


class UsedcarSellEnquiry(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    evaluation_type = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    scheduled_at = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    vehicle_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_number = models.CharField(max_length=255, blank=True, null=True)
    vehicle_variant = models.CharField(max_length=255, blank=True, null=True)
    year_of_registration = models.CharField(
        max_length=255, blank=True, null=True)

    
    class Meta:
        verbose_name = 'USED CAR - SELL'
        verbose_name_plural = 'USED CAR - SELL'