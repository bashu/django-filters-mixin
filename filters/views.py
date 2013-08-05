# -*- coding: utf-8 -*-

from django_filters import views as filters_views


class FilterMixin(filters_views.FilterMixin):

    def get_filterset_kwargs(self, filterset_class):
        kwargs = super(FilterMixin, self).get_filterset_kwargs(filterset_class)
        if kwargs['data'] is not None and 'page' in kwargs['data']:
            data = kwargs['data'].copy() ; del data['page']
            kwargs['data'] = data
        return kwargs
