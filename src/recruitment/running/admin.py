from django.contrib import admin

from .models import Cities, Countries, Regions, States


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    def get_readonly_fields(self, request, obj=None):
        return (
            list(self.readonly_fields)
            + [field.name for field in obj._meta.fields]
            + [field.name for field in obj._meta.many_to_many]
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


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
