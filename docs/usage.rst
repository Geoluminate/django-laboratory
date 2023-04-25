=====
Usage
=====

To use Django Laboratory in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'laboratory.apps.LaboratoryConfig',
        ...
    )

Add Django Laboratory's URL patterns:

.. code-block:: python

    from laboratory import urls as laboratory_urls


    urlpatterns = [
        ...
        url(r'^', include(laboratory_urls)),
        ...
    ]
