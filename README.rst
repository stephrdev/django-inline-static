django-inline-static
====================

.. image:: https://img.shields.io/pypi/v/django-inline-static.svg
   :target: https://pypi.org/project/django-inline-static/
   :alt: Latest Version

.. image:: https://codecov.io/gh/moccu/django-inline-static/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/moccu/django-inline-static
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-inline-static/badge/?version=latest
   :target: https://django-inline-static.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/moccu/django-inline-static.svg?branch=master
   :target: https://travis-ci.org/moccu/django-inline-static


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

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test


Resources
---------

* `Documentation <https://django-inline-static.readthedocs.org/>`_
* `Bug Tracker <https://github.com/moccu/django-inline-static/issues>`_
* `Code <https://github.com/moccu/django-inline-static/>`_
