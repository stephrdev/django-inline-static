import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('inline_static').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-inline-static',
    version=VERSION,
    description=(
        'django-inline-static provides template tags to inline css and '
        'javascript files in Django templates.'
    ),
    long_description=long_description,
    url='https://github.com/moccu/django-inline-static',
    project_urls={
        'Bug Reports': 'https://github.com/moccu/django-inline-static/issues',
        'Source': 'https://github.com/moccu/django-inline-static',
    },
    author='Moccu GmbH & Co. KG',
    author_email='info@moccu.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[],
    include_package_data=True,
    keywords='django static templates',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
