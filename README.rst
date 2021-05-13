django-inline-static
====================

.. image:: https://img.shields.io/pypi/v/django-inline-static.svg
   :target: https://pypi.org/project/django-inline-static/
   :alt: Latest Version

.. image:: https://github.com/stephrdev/django-inline-static/workflows/Test/badge.svg?branch=master
   :target: https://github.com/stephrdev/django-inline-static/actions?workflow=Test
   :alt: CI Status

.. image:: https://codecov.io/gh/stephrdev/django-inline-static/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/stephrdev/django-inline-static
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-inline-static/badge/?version=latest
   :target: https://django-inline-static.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status


*django-inline-static* provides template tags to inline css and javascript files in
Django templates, also corrects relative urls in css "url()" calls.


Features
--------

* Template tag to inline any static file ``inline_staticfile``
* Template tag to inline javascript files ``inline_javascript``
* Template tag to inline css files ``inline_style``
* relative to absolute path converter for paths in css files


Requirements
------------

django-inline-static supports Python 3 only and requires at least Django 1.11.


Prepare for development
-----------------------

A Python 3 interpreter is required in addition to poetry.

.. code-block:: shell

    $ poetry install


Now you're ready to run the tests:

.. code-block:: shell

    $ make tests
