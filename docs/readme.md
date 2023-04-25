# Django Laboratory 

[![Github Build](https://github.com/SSJenny90/django-laboratory/actions/workflows/build.yml/badge.svg)](https://github.com/SSJenny90/django-laboratory/actions/workflows/build.yml)
[![Github Docs](https://github.com/SSJenny90/django-laboratory/actions/workflows/docs.yml/badge.svg)](https://github.com/SSJenny90/django-laboratory/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/SSJenny90/django-laboratory/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/SSJenny90/django-laboratory)
![GitHub](https://img.shields.io/github/license/SSJenny90/django-laboratory)
![GitHub last commit](https://img.shields.io/github/last-commit/SSJenny90/django-laboratory)
![PyPI](https://img.shields.io/pypi/v/django-laboratory)
<!-- [![RTD](https://readthedocs.org/projects/django-laboratory/badge/?version=latest)](https://django-laboratory.readthedocs.io/en/latest/readme.html) -->
<!-- [![Documentation](https://github.com/SSJenny90/django-laboratory/actions/workflows/build-docs.yml/badge.svg)](https://github.com/SSJenny90/django-laboratory/actions/workflows/build-docs.yml) -->
<!-- [![PR](https://img.shields.io/github/issues-pr/SSJenny90/django-laboratory)](https://github.com/SSJenny90/django-laboratory/pulls)
[![Issues](https://img.shields.io/github/issues-raw/SSJenny90/django-laboratory)](https://github.com/SSJenny90/django-laboratory/pulls) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/django-laboratory) -->
<!-- ![PyPI - Status](https://img.shields.io/pypi/status/django-laboratory) -->

A scientific laboratory management app for Django

Documentation
-------------

The full documentation is at https://ssjenny90.github.io/django-laboratory/

Quickstart
----------

Install Django Laboratory::

    pip install django-laboratory

Add it to your `INSTALLED_APPS`:


    INSTALLED_APPS = (
        ...
        'laboratory',
        ...
    )

Add Django Laboratory's URL patterns:

    urlpatterns = [
        ...
        path('', include("laboratory.urls")),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

