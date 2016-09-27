django-exchange-themes
======================

|Build Status|

django-exchange-themes is an appearance application that allows
administrators the ability to select a predefined theme or customize
their own theme.

The license for this matches the license found for
`colorfield <https://github.com/h3/django-colorfield>`__, which is BSD
License and listed in the classifiers section of setup.py. The author
has also been added to the setup.py of django-exchange-themes.

Installation
------------

1. pip install

   ::

       pip install git+git://github.com/boundlessgeo/django-exchange-themes@master#egg=appearance

2. Add the following to your Django configuration (settings) file

   ::

       INSTALLED_APPS = (
       'appearance',
       ) + INSTALLED_APPS

3. Run migrations

   ::

       python manage.py migrate

4. Collect static

   ::

       python manage.py collectstatic --noinput

Coverage
--------

coverage within the app

::

    virtualenv venv
    source venv/bin/activate
    pip install .
    pip install coverage
    cd appearance/tests
    python manage.py migrate
    python manage.py collectstatic --noinput
    coverage run manage.py test appearance

The ``Theme model`` has the following fields:

**name** (Theme name)

-  CharField
-  Max length is 28

**description** (Theme description)

-  CharField
-  Max length is 64

**default\_theme** (Default application included Theme)

-  BooleanField
-  Not editable in Admin console

**active\_theme** (Enables Theme to be active)

-  BooleanField

**title** (Theme landing page title)

-  CharField
-  Max length is 32
-  Can be blank

**tagline** (Theme landing page tagline)

-  CharField
-  Max length is 64
-  Can be blank

**running\_hex** (Header/Footer color)

-  ColorField (GUI to select the color)
-  Default is 0F1A2C

**running\_text\_hex** (Header/Footer text color)

-  ColorField (GUI to select the color)
-  Default is FFFFFF

**running\_link\_hex** (Header/Footer link color)

-  ColorField (GUI to select the color)
-  Default is 0F1A2C

**pb\_text** (Powered by text)

-  CharField
-  Max length is 64
-  Default is 'Boundless Spatial'

**pb\_link** (Powered by link)

-  URLField
-  Default is 'http://boundlessgeo.com/'

**docs\_link** (Documentation links)

-  URLField
-  Can be blank

**background\_logo** (Landing page background image)

-  ImageField
-  Can be blank

**primary\_logo** (Landing page primary logo)

-  ImageField
-  Can be blank

**banner\_logo** (Header logo)

-  ImageField
-  Can be blank

**Note:** The templates in appearance/templates will override existing
templates in exchange. Blank fields will be accounted for and use the
default settings in the template, which are Boundless Exchange defaults.

.. |Build Status| image:: https://travis-ci.org/boundlessgeo/django-exchange-themes.svg?branch=master
   :target: https://travis-ci.org/boundlessgeo/django-exchange-themes
