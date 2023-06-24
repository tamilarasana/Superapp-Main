from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User

class Promotion(models.Model):
    DESCRIPTION = models.CharField(max_length=255)
    DISCOUNT = models.FloatField()


class Category(models.Model):
    CATEGORY_MODEL =  'models'
    CATEGORY_VARIENT =  'varients'
    CATEGORY_DETAIL =  'details'
    CATEGORY_USEDCAR =  'Used Cars'
    CATEGORY_THANKYOU =  'thankyou'

    CATEGORY_CHOICES = [
        (CATEGORY_MODEL, 'models'),
        (CATEGORY_VARIENT, 'varients'),
        (CATEGORY_DETAIL, 'details'),
        (CATEGORY_USEDCAR, 'Used Cars'),
        (CATEGORY_THANKYOU, 'thankyou')
    ]
    
    ACTIVE =  'Active'
    INACTIVE =  'Inactive'
    
    ACTIVE_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    ]

    TITLE = models.CharField(max_length=255)
    DESCRIPTION = models.CharField(max_length=255)
    PAGE_NAVIGATION = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default=CATEGORY_MODEL)
    IMAGE = models.ImageField(
        upload_to='store/images')
    BANNERS = models.JSONField(null=True, blank=True)    
    SEARCH_KEYWORD = models.CharField(max_length=255, null=True, blank=True)
    PREFIX_KEYWORD = models.CharField(max_length=255, null=True, blank=True)
    POSITION = models.IntegerField(null=True, blank=True, unique=True)
    ACTIVE_STATUS = models.CharField(max_length=15, choices=ACTIVE_CHOICES, default=ACTIVE)

    def __str__(self) -> str:
        return self.TITLE

    class Meta:
        ordering = ['TITLE']
        verbose_name = 'CHANNELS'
        verbose_name_plural = 'CHANNELS' 


class Itemlist(models.Model):
    CATEGORY_MODEL =  'models'
    CATEGORY_VARIENT =  'varients'
    CATEGORY_DETAIL =  'details'
    CATEGORY_USEDCAR =  'Used Cars'
    CATEGORY_THANKYOU =  'thankyou'


    CATEGORY_CHOICES = [
        (CATEGORY_MODEL, 'models'),
        (CATEGORY_VARIENT, 'varients'),
        (CATEGORY_DETAIL, 'details'),
        (CATEGORY_USEDCAR, 'Used Cars'),
        (CATEGORY_THANKYOU, 'thankyou')
    ]
    TITLE = models.CharField(max_length=255)
    NAME = models.CharField(max_length=255, null=True, blank=True)
    SLUG = models.SlugField()
    DESCRIPTION = models.TextField(null=True, blank=True)
    IMAGES = models.JSONField(null=True, blank=True)
    PRICE = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    CATEGORY = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='items')
    PAGE_NAVIGATION = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default=CATEGORY_MODEL)
    SEARCH_KEYWORD = models.CharField(max_length=255, null=True, blank=True)
    PROMOTIONS = models.ManyToManyField(Promotion, blank=True)

    def __str__(self) -> str:
        return self.TITLE

    class Meta:
        ordering = ['TITLE']
        verbose_name = 'ITEMS'
        verbose_name_plural = 'ITEMS'      


class ItemDescription(models.Model):

    CATEGORY_MODEL =  'models'
    CATEGORY_VARIENT =  'varients'
    CATEGORY_DETAIL =  'details'
    CATEGORY_USEDCAR =  'Used Cars'
    CATEGORY_THANKYOU =  'thankyou'


    CATEGORY_CHOICES = [
        (CATEGORY_MODEL, 'models'),
        (CATEGORY_VARIENT, 'varients'),
        (CATEGORY_DETAIL, 'details'),
        (CATEGORY_USEDCAR, 'Used Cars'),
        (CATEGORY_THANKYOU, 'thankyou')
    ]
    TITLE_FOR_PRICE = models.CharField(max_length=255, blank=True, null=True)
    TITLE = models.CharField(max_length=255)
    SUBTITLE = models.CharField(max_length=255, null=True, blank=True)
    COLOR = models.CharField(max_length=255)
    EX_PRICE = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    PRICE = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    IMAGES = models.JSONField(null=True, blank=True)
    DESCRIPTION = models.TextField(null=True, blank=True)
    ABOUT = models.TextField(null=True, blank=True)
    ITEMLIST = models.ForeignKey(
        Itemlist, on_delete=models.PROTECT, related_name='itemlist')  
    PAGE_NAVIGATION = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default=CATEGORY_MODEL)

    def __str__(self) -> str:
        return self.TITLE

    class Meta:
        ordering = ['TITLE'] 
        verbose_name = 'ITEM DESCRIPTION'
        verbose_name_plural = 'ITEM DESCRIPTION' 


class ItemDescSpec(models.Model):
    ITEM_DESC = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, related_name='spec')
    ITEM_SPEC = models.CharField(max_length=255)
    VALUE = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.ITEM_DESC.TITLE

    class Meta:
        ordering = ['ITEM_DESC']  
        verbose_name = 'SPECIFICATIONS'
        verbose_name_plural = 'SPECIFICATIONS' 
