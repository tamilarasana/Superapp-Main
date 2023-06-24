from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(AppBooking)
class AppBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['PROFILE', 'ITEMLIST', 'CREATED_AT',
                    'PAYMENT_STATUS', 'PAYMENT_ID', 'AMOUNT', 'CRMID']


@admin.register(NewCarBooking)
class NewCarBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['NAME', 'EMAIL', 'MOBILE', 'PROFILE', 'ADDRESS', 'ITEM_DESCRIPTION',
                    'BOOKING_ID', 'CITY', 'OUTLETS', 'ITEM_PRICE', 'EMPLOYEE_ID', 'REFERRED_BY', 'BOOKING_STATUS']


@admin.register(UsedCarBooking)
class UsedCarBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ITEMLIST', 'ITEM_DESCRIPTION', 'BOOKING_ID', 'PROFILE', 'ADDRESS', 'BRAND', 'MODEL', 'TRANSMISSION', 'FUEL', 'YEAR', 'PHONE', 'EMAIL',
                    'KMS_DRIVEN_STARTING', 'KMS_DRIVEN_ENDING', 'PRICE', 'LAT', 'LONG', 'ENQUIRE_AT', 'SCHEDULED', 'EMPLOYEE_ID', 'REFERRED_BY', 'BOOKING_STATUS']


@admin.register(UsedcarSellEnquiry)
class UsedcarSellEnquiryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['address', 'evaluation_type', 'mobile_no', 'name', 'pincode', 'scheduled_at',
                    'brand', 'vehicle_model', 'vehicle_number', 'vehicle_variant', 'year_of_registration']


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['BOOKING_ID', 'ITEMLIST', 'ITEM_DESCRIPTION', 'PROFILE', 'ADDRESS', 'NAME', 'EMAIL', 'MOBILE', 'CITY', 'OUTLET',
                    'MODEL', 'VARIENT', 'COLOR', 'PICKUP_SLOT', 'ITEM_PRICE', 'EMPLOYEE_ID', 'REFERRED_ID', 'DELIVERRED_TIME', 'BOOKING_STATUS']


@admin.register(Accessory)
class AccessoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['BOOKING_ID', 'ITEMLIST', 'ITEM_DESCRIPTION', 'PROFILE',
                    'ADDRESS', 'ITEM_PRICE', 'DELIVERRED_TIME', 'BOOKING_STATUS']


@admin.register(Insurance)
class InsuranceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ITEMLIST', 'ITEM_DESCRIPTION', 'PROFILE', 'ADDRESS', 'NAME', 'EMAIL', 'MOBILE', 'REGISTERED_NUMBER', 'MODEL', 'VARIANT',
                    'FUEL', 'REG_DATE', 'POLICY_EXPIRE_DATE', 'LAST_CLAIM_STATUS', 'CLAIM_BONUS', 'EMPLOYEE_ID', 'REFFERED_BY', 'BOOKED_AT', 'BOOKING_STATUS']


