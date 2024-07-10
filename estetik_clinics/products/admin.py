from django.contrib import admin

from products.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'discount', 'category',
                    'manufacturer']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']


@admin.register(CharacteristicValue)
class CharacteristicValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'characteristic']


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'created_at', 'phone_number', 'status',
                    'total_price']
    list_filter = ['status']
    inlines = [OrderItemInline]


@admin.register(ProductImage)
class productImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']

