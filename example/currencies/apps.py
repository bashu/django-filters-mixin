from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CurrenciesConfig(AppConfig):
    name = "currencies"
    verbose_name = _("Currencies")
    default_auto_field = "django.db.models.AutoField"
