from django.db import models
from django.utils.translation import gettext as _


class Laboratory(models.Model):
    __doc__ = _("A collection/laboratory of scientific instruments.")

    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
        help_text=_("Name of the laboratory or collection of instruments."),
    )
    description = models.TextField(
        _("description"),
        help_text=_(
            "A short description of the laboratory. Try to include information such as the purpose of the laboratory, what data does it collect, where it is located, etc."
        ),
    )

    contact_name = models.CharField(
        _("contact name"),
        max_length=255,
        help_text=_("Full name of the laboratory point-of-contact."),
    )
    contact_email = models.EmailField(
        _("contact email"),
        help_text=_("A point-of-contact email to get in touch with the laboratory."),
        null=True,
        blank=True,
    )

    outputs = models.ManyToManyField(
        "laboratory.DataType",
        verbose_name=_("output types"),
        help_text=_("Types of data that this laboratory outputs."),
    )

    class Meta:
        db_table = "laboratory_laboratory"
        verbose_name = _("laboratory")
        verbose_name_plural = _("laboratories")

    def __str__(self):
        return f"{self.name}"


class Manufacturer(models.Model):
    __doc__ = _("Stores manufacturers of scientific instruments.")

    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
        help_text=_("Name of the manufacturer."),
        unique=True,
    )
    location = models.CharField(
        max_length=255,
        verbose_name=_("location"),
        help_text=_("Location of the manufacturer. E.g. country, city etc."),
    )

    class Meta:
        db_table = "laboratory_manufacturer"
        verbose_name = _("manufacturer")
        verbose_name_plural = _("manufacturers")

    def __str__(self):
        return f"{self.name}"


class Instrument(models.Model):
    __doc__ = _("An instrument used for the collection of scientific data.")

    laboratory = models.ForeignKey(
        "laboratory.Laboratory",
        verbose_name=_("laboratory"),
        help_text=_("The laboratory to which the instrument belongs."),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    internal_id = models.CharField(
        max_length=255,
        verbose_name=_("internal ID"),
        help_text=_(
            "Unique internal ID of the instrument used by the laboratory. "
            "Required to distinguish multiple instruments of the same type "
            "in a single laboratory."
        ),
    )

    type = models.ForeignKey(
        "laboratory.InstrumentType",
        verbose_name=_("instrument type"),
        help_text=_("The laboratory to which the instrument belongs."),
        on_delete=models.PROTECT,
    )

    class Meta:
        db_table = "laboratory_instrument"
        verbose_name = _("instrument")
        verbose_name_plural = _("instruments")
        default_related_name = "instruments"
        unique_together = ("laboratory", "type", "internal_id")


class InstrumentType(models.Model):
    """Stores specific instrument types for a given manufacturer."""

    type = models.CharField(
        max_length=255,
        verbose_name=_("instrument type"),
        help_text=_("The type of instrument."),
    )
    model = models.CharField(
        max_length=255,
        verbose_name=_("instrument model"),
        help_text=_("Specific model name of this instrument type."),
    )
    manufacturer = models.ForeignKey(
        "laboratory.Manufacturer",
        verbose_name=_("manufacturer"),
        help_text=_("The manufacturer of the instrument."),
        related_name="instruments",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    year_manufactured = models.PositiveSmallIntegerField(
        verbose_name=_("year manufactured"),
        help_text=_("Year of manufacture of the instrument."),
    )
    description = models.TextField(
        _("description"),
        help_text=_("Provide a short description of this particular instrument type."),
    )

    collects = models.ManyToManyField(
        "laboratory.DataType",
        verbose_name=_("collects"),
        help_text=_("Types of data that this instrument collects."),
    )

    class Meta:
        db_table = "laboratory_instrument_type"
        verbose_name = _("instrument type")
        verbose_name_plural = _("instrument types")
        unique_together = ("manufacturer", "model", "year_manufactured")

    def __str__(self):
        return f"{self.manufacturer} <{self.model}>: {self.type}"


class DataType(models.Model):
    """Stores unique data types that are collected by instruments or
    output by laboratories."""

    type = models.CharField(
        _("data type"),
        max_length=255,
        help_text=_("Specify a type of data."),
        unique=True,
    )

    class Meta:
        db_table = "laboratory_data_type"
        verbose_name = _("data type")
        verbose_name_plural = _("data types")

    def __str__(self):
        return f"{self.type}"
