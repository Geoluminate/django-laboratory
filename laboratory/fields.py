"""This module contains fields that you can use in your projects to link
database entries to a collection (laboratory) of scientific instruments.
The fields are not special in any way but provide a direct relationship
to the `laboratory.Laboratory` model.

    from django.db import models
    from laboratory.fields import LaboratoryFK, LaboratoryM2M

    class Dataset(models.Model):

        name = models.CharField()
        description = models.TextField()
        license = License()

"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Laboratory(models.ForeignKey):
    """A foreign key field to the `license.License` model"""

    def __init__(self, *args, **kwargs):
        kwargs["to"] = "laboratory.Laboratory"
        kwargs["verbose_name"] = _("laboratory")
        super().__init__(*args, **kwargs)


class LaboratoryM2M(models.ManyToManyField):
    """A many-to-many field to the `license.License` model"""

    def __init__(self, *args, **kwargs):
        kwargs["to"] = "laboratory.Laboratory"
        kwargs["verbose_name"] = _("laboratory")
        super().__init__(*args, **kwargs)
