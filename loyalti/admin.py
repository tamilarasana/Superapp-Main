from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
@admin.register(Loyalti)
class LoyaltiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['PROFILE', 'BALANCE_POINTS', 'TOTAL_EARNED_POINTS',
                    'LAST_UPDATED_POINTS', 'BUSINESS_TURNOVER']


@admin.register(LoyaltiTransaction)
class LoyaltiTransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['PROFILE', 'LOYALTI', 'AMOUNT',
                    'STATUS', 'TIME_OF_TRANSACTION', 'TRANSACTION_TYPE']


@admin.register(LoyaltiEntity)
class LoyaltiEntityAdmin(admin.ModelAdmin):
    list_display = ['CATEGORY', 'POINTS_ADD_PER_100', 'TIME_OF_UPDATE']
