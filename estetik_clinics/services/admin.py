from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

from services.models import *


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'order', 'title')
    list_display_links = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'is_home_page']


@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'service']


@admin.register(Characteristic)
class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'value', 'service']


@admin.register(ProcedureCost)
class ProcedureCostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'service']













