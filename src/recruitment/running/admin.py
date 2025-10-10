from django.contrib import admin

from .models import Area, Cities, Continents, Countries, Regions

# Register your models here.

admin.site.register(Area)
admin.site.register(Cities)
admin.site.register(Continents)
admin.site.register(Countries)
admin.site.register(Regions)
