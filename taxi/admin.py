from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser

from taxi.models import Manufacturer, Car, Driver


admin.site.register(Manufacturer)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", "display_drivers"]
    list_filter = [
        "manufacturer",
    ]
    search_fields = [
        "drivers",
    ]

    @admin.display(description="Drivers")
    def display_drivers(self, obj):
        return ", ".join(driver.username for driver in obj.drivers.all())


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
