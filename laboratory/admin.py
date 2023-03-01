from django.contrib import admin
from django.db.models import Count

from .models import DataType, Instrument, InstrumentType, Laboratory, Manufacturer


class InstrumentInline(admin.StackedInline):
    model = Instrument
    extra = 0


# class InstrumentInline(admin.TabularInline):
#     model = Instrument
#     extra = 1


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    inlines = [InstrumentInline]
    list_display = [
        "name",
        "description",
        "contact_name",
        "contact_email",
        "_instruments",
        "_outputs",
    ]
    list_filter = ["outputs"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(Count("instruments"))

    def _instruments(self, obj):
        return obj.instruments__count

    def _outputs(self, obj):
        return ", ".join(d.type for d in obj.outputs.all())


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name",
        "location",
        "_instruments",
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(Count("instruments"))

    def _instruments(self, obj):
        # print(obj.__dict__)
        return obj.instruments__count


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = [
        "internal_id",
        "type",
        "laboratory",
    ]
    list_filter = ["type", "laboratory"]

    search_fields = [
        "laboratory__name",
        "type__manufacturer",
        "type__type",
        "internal_id",
    ]


admin.site.register(DataType, admin.ModelAdmin)


@admin.register(InstrumentType)
class InstrumentTypeAdmin(admin.ModelAdmin):
    list_display = ["type", "model", "manufacturer", "year_manufactured", "_collects"]
    list_filter = ["manufacturer"]

    def _collects(self, obj):
        return ", ".join(d.type for d in obj.collects.all())
