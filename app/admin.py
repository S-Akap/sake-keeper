from django.contrib import admin
from .models import Restaurant, BottleManagement, Bottle

class RestaurantAdmin(admin.ModelAdmin):
    list_display=["pk", "name", "address", "create_user"]

class BottleManagementAdmin(admin.ModelAdmin):
    list_display=["pk", "management_name", "customer", "restaurant"]

class BottleAdmin(admin.ModelAdmin):
    list_display=["pk", "management", "liquor_type", "bottle_name", "purchase_date", "storage_period", "is_empty"]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(BottleManagement, BottleManagementAdmin)
admin.site.register(Bottle, BottleAdmin)