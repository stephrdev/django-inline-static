Usage
=====

Loading static files
--------------------

To inline any static file in your template, use the ``inline_staticfile`` tag.
The inlined content is not marked safe, do this by yourself if you're sure that
the included content is safe for html documents.

.. code-block:: text

    {% load inline_static_tags %}

    {% inline_staticfile 'build/fake.txt' %}

    <!-- or -->

    {% inline_staticfile 'build/image.svg' as image %}{{ image|safe }}


Inlining javascript
-------------------

If you want to inline javascript code, use the ``inline_javascript`` tag.
The inlined content will be marked as safe.

.. code-block:: text

    {% load inline_static_tags %}

    <script>{% inline_javascript 'build/critical.pkg.js' %}</script>


Inlining styles
---------------

To inline a css styles file, use the ``inline_style`` template tag.

The styles will be transformed by replacing any relative url in the content with
absolute urls to make sure fonts, background images and other ``url()`` calls
work after including.

.. code-block:: text

    {% load inline_static_tags %}

    <style type="text/css">{% inline_style 'build/all.css' %}</style>
