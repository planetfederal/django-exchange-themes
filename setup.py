import os
from setuptools import setup, find_packages

with open('README.rst', 'r') as inp:
    LONG_DESCRIPTION = inp.read()

setup(
    name='django-exchange-themes',
    version='1.0.2',
    author='Boundless Spatial, Maxime Haineault (django-colorfield)',
    author_email='contact@boundlessgeo.com',
    url='https://github.com/boundlessgeo/django-exchange-themes',
    download_url="https://github.com/boundlessgeo/django-exchange-themes",
    description="A Django Application for Boundless Exchange Themes.",
    long_description=LONG_DESCRIPTION,
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django >=1.8.7, < 1.9a0",
        "pillow>=3.1.1",
        "python-resize-image==1.1.10"
    ],
    zip_safe=False,
    classifiers=[
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django :: 1.8',
    ]
)
