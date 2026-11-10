Changes
-------

0.2.0 (unreleased)
~~~~~~~~~~~~~~~~~~

* Now requires Python 3.11+ and Django 5.2+. Python 2 and older Django
  versions are no longer supported.
* Removed ``filters.__version__``; use
  ``importlib.metadata.version("django-filters-mixin")`` instead.
* Migrated packaging to ``pyproject.toml``, added a pytest test suite,
  pre-commit hooks and GitHub Actions CI/release workflows.
* Updated the ``example`` project to work with current Django versions.

0.1.4 (2016-10-14)
~~~~~~~~~~~~~~~~~~

* Updated to Django 1.10.x.
