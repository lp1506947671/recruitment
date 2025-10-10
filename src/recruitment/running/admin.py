from django.contrib import admin

from .models import Cities, Countries, Regions, States


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


@admin.register(Countries)
class CountriesAdmin(ReadOnlyAdmin):
    search_fields = ("cname",)


@admin.register(States)
class StatesAdmin(ReadOnlyAdmin):
    search_fields = ("cname",)
    autocomplete_fields = [
        "country_id",
    ]


@admin.register(Cities)
class CitiesAdmin(ReadOnlyAdmin):
    search_fields = ("cname",)
    autocomplete_fields = [
        "state_id",
    ]


@admin.register(Regions)
class RegionsAdmin(ReadOnlyAdmin):
    search_fields = ("cname",)
    autocomplete_fields = [
        "city_id",
    ]
