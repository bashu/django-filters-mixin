Changes
-------

0.2.1 (2026-11-13)
~~~~~~~~~~~~~~~~~~

* Switched the build backend from setuptools to hatchling and moved the
  package to the ``src`` layout. The import path ``filters`` is unchanged.
* Moved the test suite out of the package into the top-level ``tests``
  directory; tests are no longer shipped in the wheel or sdist.
* Removed the ``example`` project.

0.2.0 (2026-11-10)
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
