from django.contrib import admin

# Register your models here.
from accounts.models import Account, Asset, Balance


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'usd_total_value')


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_name', 'usd_value')


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'account_name', 'asset_name')

    def account_name(self, obj):
        """
        used for nicer column name representation
        """
        return obj.account_id

    def asset_name(self, obj):
        """
        used for nicer column name representation
        """
        return obj.asset_id
