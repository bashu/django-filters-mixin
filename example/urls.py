from django import forms
from django.utils.translation import ugettext
from django.conf.urls import url

import django_filters
from django_filters.filters import OrderingFilter

from currencies.models import Currency

from filters.views import FilterMixin

ORDER_BY_FIELD = 'o'

class CurrencyFilterForm(forms.Form):

    def __init__(self, data={}, *args, **kwargs):
        super(CurrencyFilterForm, self).__init__(data, *args, **kwargs)  # NOQA
        try:
            self.fields[ORDER_BY_FIELD].widget.attrs = {
                'onchange': "this.form.submit();",
            }
        except KeyError:
            pass


class CurrencyFilter(django_filters.FilterSet):

    o = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('code', 'code'),
        ),

        # labels do not need to retain order
        field_labels={
            'code': ugettext("A-Z"),
            '-code': ugettext("Z-A"),
        }
    )

    class Meta:  # pylint: disable=C1001
        form = CurrencyFilterForm
        model = Currency
        fields = []


class CurrencyListView(FilterMixin, django_filters.views.FilterView):
    model = Currency
    paginate_by = 12
    filterset_class = CurrencyFilter


urlpatterns = [
    url(r'^$', CurrencyListView.as_view()),
]
