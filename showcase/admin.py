from django.contrib import admin, messages
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from . import models
from django import forms


@admin.register(models.Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['TITLE', 'DESCRIPTION', 'PAGE_NAVIGATION', 'POSITION']
    search_fields = ['TITLE']
    list_editable = ['POSITION']


class ItemDescSpecInline(admin.TabularInline):
    model = models.ItemDescSpec


class ItemlistResource(resources.ModelResource):
    category = fields.Field(column_name='category_id',
                            attribute='category', widget=ForeignKeyWidget(models.Category))

    class Meta:
        model = models.Itemlist
        import_id_fields = ['title']
        fields = ('title', 'slug', 'description', 'images', 'price',
                  'category', 'page_navigation', 'search_keyword')
        export_order = fields


class ItemDescriptionResource(resources.ModelResource):
    category = fields.Field(column_name='itemlist_id',
                            attribute='itemlist', widget=ForeignKeyWidget(models.Itemlist))

    class Meta:
        model = models.ItemDescription
        import_id_fields = ['title']
        fields = ('title', 'color', 'images', 'description',
                  'about', 'itemlist', 'page_navigation')
        export_order = fields


@admin.register(models.Itemlist)
class ItemlistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    autocomplete_fields = ['CATEGORY']
    prepopulated_fields = {
        'SLUG': ['TITLE']
    }
    list_display = ['TITLE', 'NAME', 'PRICE',
                    'CATEGORY_TITLE', 'PAGE_NAVIGATION']
    list_editable = ['PRICE']
    list_filter = ['CATEGORY']
    list_per_page = 10
    list_select_related = ['CATEGORY']
    search_fields = ['TITLE']
    resources_class = ItemlistResource

    def CATEGORY_TITLE(self, itemlist):
        return itemlist.CATEGORY.TITLE

    class Media:
        css = {
            'all': ['show/styles.css']
        }


@admin.register(models.ItemDescription)
class ItemDescriptionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    autocomplete_fields = ['ITEMLIST']
    inlines = [ItemDescSpecInline]
    list_display = ['TITLE', 'PRICE', 'ITEMLIST_TITLE']
    list_editable = ['PRICE']
    list_filter = ['ITEMLIST']
    list_per_page = 10
    list_select_related = ['ITEMLIST']
    search_fields = ['TITLE']
    resources_class = ItemDescriptionResource

    def ITEMLIST_TITLE(self, itemlist):
        return itemlist.TITLE

    class Media:
        css = {
            'all': ['show/styles.css']
        }


class ItemDescSpecResource(resources.ModelResource):
    itemlist = fields.Field(column_name='item_desc_id',
                            attribute='item_desc', widget=ForeignKeyWidget(models.Itemlist))

    class Meta:
        model = models.ItemDescription
        import_id_fields = ['title']
        fields = ('title', 'subtitle', 'color', 'images',
                  'description', 'about', 'itemlist', 'page_navigation')
        export_order = fields


@admin.register(models.ItemDescSpec)
class ItemDescSpecAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ITEM_DESC', 'ITEM_SPEC', 'VALUE']
    search_fields = ['ITEM_DESC']
    resources_class = ItemDescSpecResource
    list_filter = ['ITEM_DESC']
