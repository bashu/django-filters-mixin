Example
=======

To run the example application, make sure you have the required
packages installed. From the root of the source checkout:

.. code-block:: bash

    uv sync

Next, set up the database and load the sample currencies:

.. code-block:: bash

    uv run python example/manage.py migrate
    uv run python example/manage.py loaddata example/initial_data.json

And run it:

.. code-block:: bash

    uv run python example/manage.py runserver

Then open http://127.0.0.1:8000/ - the list of currencies is paginated
and can be ordered with the drop-down, and both work together.

Good luck!
