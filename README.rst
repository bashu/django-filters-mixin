django-filters-mixin
====================

Simple integration between django-filter_ and pagination_

.. image:: https://img.shields.io/pypi/v/django-filters-mixin.svg
    :target: https://pypi.python.org/pypi/django-filters-mixin/

.. image:: https://img.shields.io/pypi/dm/django-filters-mixin.svg
    :target: https://pypi.python.org/pypi/django-filters-mixin/

.. image:: https://img.shields.io/github/license/bashu/django-filters-mixin.svg
    :target: https://pypi.python.org/pypi/django-filters-mixin/

Requirements
------------

You must have *django-filter* installed and configured, see the
django-filter_ documentation for details and setup instructions.

Installation
============

.. code-block:: shell

    pip install django-filters-mixin


Usage
=====

The ``FilterMixin`` allows to use pagination together with filtering

.. code-block:: python

    # views.py

    import django_filters
    from filters.views import FilterMixin


    class CustomFilterSet(django_filters.FilterSet):
        # read https://github.com/alex/django-filter#usage
        ...


    class CustomFilterView(FilterMixin, django_filters.views.FilterView):
        filterset_class = CustomFilterSet
        paginate_by = 12
        ...


Please see ``example`` application. This application is used to
manually test the functionalities of this package. This also serves as
good example...

You need Django 1.4 or above to run that. It might run on older
versions but that is not tested.

.. _django-filter: https://github.com/alex/django-filter
.. _pagination: https://docs.djangoproject.com/en/dev/topics/pagination/
