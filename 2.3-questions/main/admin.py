from django.contrib import admin

from .models import Category, Order, OrderItems, Product


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    fields = ['product', 'quantity']
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]


admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
