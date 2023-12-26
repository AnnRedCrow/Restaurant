from django.contrib import admin
from core.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


class DishAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description', 'price', 'is_recommended', 'is_published', 'dish_image']


class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ['paid_status', 'status']
    list_filter = ('paid_status', 'order_date')
    list_display = ['user', 'price', 'paid_status', 'status', 'order_date']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice', 'item', 'image', 'quantity', 'price', 'total']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'is_default']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Address, AddressAdmin)
