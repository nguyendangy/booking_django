from django.contrib import admin

from users.models import User, Address


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'is_active', 'is_staff',)
    search_fields = ('phone',)

    def delete_queryset(self, request, queryset):
        Address.objects.filter(phone__in=[item.phone for item in queryset]).delete()
        queryset.delete()


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone',)
    search_fields = ('phone',)


admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
