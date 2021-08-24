from django.contrib import admin
from store.models import Tshirt, Brand, Color, IdealFor, NeckType, Occasion, Sleeve, SizeVariant
# Register your models here.

# class SizeVariantConfiguration(admin.StackedInline):
#     model = SizeVariant
    
class SizeVariantConfiguration(admin.TabularInline):
    model = SizeVariant   
class TshirtConfiguratiion(admin.ModelAdmin):
    inlines = [SizeVariantConfiguration]

admin.site.register(Tshirt, TshirtConfiguratiion)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(IdealFor)
admin.site.register(NeckType)
admin.site.register(Occasion)
admin.site.register(Sleeve)
# admin.site.register(SizeVariant)
