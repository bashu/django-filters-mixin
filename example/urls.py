from django import forms
from django.urls import path
from django.utils.translation import gettext_lazy as _

import django_filters
from currencies.models import Currency
from django_filters.filters import OrderingFilter
from django_filters.views import FilterView

from filters.views import FilterMixin

ORDER_BY_FIELD = "o"


class CurrencyFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if ORDER_BY_FIELD in self.fields:
            self.fields[ORDER_BY_FIELD].widget.attrs = {
                "onchange": "this.form.submit();",
            }


class CurrencyFilter(django_filters.FilterSet):
    o = OrderingFilter(
        # tuple-mapping retains order
        fields=(("code", "code"),),
        # labels do not need to retain order
        field_labels={
            "code": _("A-Z"),
            "-code": _("Z-A"),
        },
    )

    class Meta:
        form = CurrencyFilterForm
        model = Currency
        fields = []


class CurrencyListView(FilterMixin, FilterView):
    model = Currency
    paginate_by = 12
    filterset_class = CurrencyFilter
    ordering = ["code"]


urlpatterns = [
    path("", CurrencyListView.as_view()),
]
