django-filters-mixin
====================

.. image:: https://badge.fury.io/py/django-filters-mixin.svg
    :target: https://badge.fury.io/py/django-filters-mixin

.. image:: https://img.shields.io/pypi/pyversions/django-filters-mixin.svg
    :target: https://pypi.python.org/pypi/django-filters-mixin/

.. image:: https://img.shields.io/pypi/djversions/django-filters-mixin.svg
    :target: https://pypi.python.org/pypi/django-filters-mixin/

.. image:: https://github.com/bashu/django-filters-mixin/actions/workflows/test.yml/badge.svg
    :target: https://github.com/bashu/django-filters-mixin/actions/workflows/test.yml

Simple integration between django-filter_ and pagination_.

Maintained by `Basil Shubin <https://github.com/bashu/>`_, and some great
`contributors <https://github.com/bashu/django-filters-mixin/contributors>`_.

Requirements
------------

You must have *django-filter* installed and configured, see the
django-filter_ documentation for details and setup instructions.

Installation
------------

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install django-filters-mixin

Usage
-----

The ``FilterMixin`` allows to use pagination together with filtering:
the ``page`` query parameter is removed from the data passed to the
filterset, so it is never treated as a filter value.

.. code-block:: python

    # views.py

    import django_filters
    from django_filters.views import FilterView

    from filters.views import FilterMixin


    class CustomFilterSet(django_filters.FilterSet):
        # read https://django-filter.readthedocs.io/en/stable/guide/usage.html
        ...


    class CustomFilterView(FilterMixin, FilterView):
        filterset_class = CustomFilterSet
        paginate_by = 12
        ...

Please see the ``example`` application. This application is used to
manually test the functionalities of this package. This also serves as
a good example.

Testing
-------

The test suite uses `pytest <https://pytest.org/>`_ and
`pytest-django <https://pytest-django.readthedocs.io/>`_, and runs entirely
against an in-memory SQLite database - no external database setup is
required::

    $ uv run --group dev pytest

For testing against the full matrix of supported Python and Django versions,
install tox (``pip install tox``) and run ``tox`` from the source checkout::

    $ tox

Contributing
------------

If you've found a bug, implemented a feature or customized the template and
think it is useful then please consider contributing. Patches, pull requests or
just suggestions are welcome!

License
-------

``django-filters-mixin`` is released under the BSD license.

.. _django-filter: https://github.com/carltongibson/django-filter
.. _pagination: https://docs.djangoproject.com/en/stable/topics/pagination/
