# django-exchange-themes

[![Build Status](https://travis-ci.org/boundlessgeo/django-exchange-themes.svg?branch=master)](https://travis-ci.org/boundlessgeo/django-exchange-themes)

django-exchange-themes is an appearance application that allows administrators
the ability to select a predefined theme or customize their own theme.

The license for this matches the license found for [colorfield](https://github.com/h3/django-colorfield), which is BSD License and listed in the classifiers section of setup.py. The author has also been added to the setup.py of django-exchange-themes.

## Installation
1. pip install
```
pip install git+git://github.com/boundlessgeo/django-exchange-themes@master#egg=appearance
```
2. Add the following to your Django configuration (settings) file
```
INSTALLED_APPS = (
    'appearance',
) + INSTALLED_APPS
```
3. Run migrations
```
python manage.py migrate
```
4. Collect static
```
python manage.py collectstatic --noinput
```

## Coverage

coverage within the app
```
virtualenv venv
source venv/bin/activate
pip install .
pip install coverage
cd appearance/tests
python manage.py migrate
python manage.py collectstatic --noinput
coverage run manage.py test appearance
```

The `Theme model` has the following fields:

+ __name__ (Theme name)
  + CharField
  + Max length is 28
+ __description__ (Theme description)
  + CharField
  + Max length is 64
+ __default_theme__ (Default application included Theme)
  + BooleanField
  + Not editable in Admin console
+ __active_theme__ (Enables Theme to be active)
  + BooleanField
+ __title__ (Theme landing page title)
  + CharField
  + Max length is 32
  + Can be blank
+ __tagline__ (Theme landing page tagline)
  + CharField
  + Max length is 64
  + Can be blank
+ __running_hex__ (Header/Footer color)
  + ColorField (GUI to select the color)
  + Default is 0F1A2C
+ __running_text_hex__ (Header/Footer text color)
  + ColorField (GUI to select the color)
  + Default is FFFFFF
+ __running_link_hex__ (Header/Footer link color)
  + ColorField (GUI to select the color)
  + Default is 0F1A2C
+ __pb_text__ (Powered by text)
  + CharField
  + Max length is 64
  + Default is 'Boundless Spatial'
+ __pb_link__ (Powered by link)
  + URLField
  + Default is 'http://boundlessgeo.com/'
+ __docs_link__ (Documentation links)
  + URLField
  + Can be blank
+ __background_logo__ (Landing page background image)
  + ImageField
  + Can be blank
+ __primary_logo__ (Landing page primary logo)
  + ImageField
  + Can be blank
+ __banner_logo__ (Header logo)
  + ImageField
  + Can be blank

__Note:__ The templates in appearance/templates will override existing templates in
exchange. Blank fields will be accounted for and use the default settings in the template, which are Boundless Exchange defaults.
