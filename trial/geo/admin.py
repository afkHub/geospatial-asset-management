from django.contrib import admin

# Register your models here.
from .models import Asset, AssetType, AssetTypeProperties, AssetTypeSymbol, AssetPropertyValues, Staffs

admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(AssetTypeProperties)
admin.site.register(AssetPropertyValues)
admin.site.register(Staffs)

admin.site.register(AssetTypeSymbol)