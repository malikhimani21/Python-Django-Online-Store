from django.contrib import admin
from store.models import Tshirt, Brand, Color, IdealFor, NeckType, Occasion, Sleeve
# Register your models here.

admin.site.register(Tshirt)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(IdealFor)
admin.site.register(NeckType)
admin.site.register(Occasion)
admin.site.register(Sleeve)
