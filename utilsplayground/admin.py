from django.contrib import admin
from .models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['TITLE']


@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = ['CITY', 'NAME']


@admin.register(PaymentMode)
class PaymentModeAdmin(admin.ModelAdmin):
    list_display = ['PAYMENT_MODE_NAME', 'STATUS']


@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ['VERSION_NAME', 'VERSION_DESCRIPTION', 'VERSION_NUMBER',
                    'VERSION_NOTES', 'VERSION_REMARKS', 'VERSION_STATUS']
