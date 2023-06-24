from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin


@admin.register(models.Banner)
class BannerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['PROMOTION_TYPE', 'TITLE',
                    'IMAGE', 'DESCRIPTION', 'PAGE_NAVIGATION']
    search_fields = ['PROMOTION_TYPE']


@admin.register(models.Promotions)
class PromotionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['TITLE', 'POSITION']
    search_fields = ['POSITION']


@admin.register(models.FeaturedItem)
class FeaturedItemAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['PROMOTION', 'PROMOTED_ITEM',
                    'DESCRIPTION', 'DISCOUNT', 'POSITION', 'PAGE_NAVIGATION']
    search_fields = ['PROMOTION']
