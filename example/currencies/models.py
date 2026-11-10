from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    code = models.CharField(_("code"), max_length=3, unique=True)
    name = models.CharField(_("name"), max_length=55)
    symbol = models.CharField(_("symbol"), max_length=4, blank=True)

    class Meta:
        ordering = ["code"]
        verbose_name = _("currency")
        verbose_name_plural = _("currencies")

    def __str__(self):
        return self.code
