# GALLERIE

This is a gallery application that displays photos based on category and location. Users can view details about the photos and copy the photo link to share with others.



## Table of contents
+ [Features](#Features)
+ [Dependancies](#Dependancies)
+ [Technology Used](#technology-used)
+ [Authors Info](#authors-info)
## App screenshot
![Gallerie](/static/images/lourve.png)
## Features

- Django 4.0+
- Uses Pipenv the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.


## Technologies used
- Back-end Framework: Django (Version 4.0.3)
- Front-end Framework: Bootstrap
- Language: Python (Version 3.8.10)
## Dependancies
In order for you to use the content on this repo ensure you have the following:

- A computer that runs on either of the following; (Windows 7+, Linux, Mac OS)
- Python 3.6+
## How to install

```bash
#clone the repo
git clone https://github.com/amani-joseph/gallerie.git
# install virtual environment
$ python3 -m venv venv
#actictvate virtual environment
$ . venv/bin/active
#Install all dependecies
$ pip install -r requirements.txt
# Make databases and make migrations
$ python manage.py makemigrations 
$ python manage.py migrate 
#create a super user
$ python manage.py rceatesuperuser 
#4. Running the application
$ python3 manage.py runserver



```
## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```
## Behavior Driven Development

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load page | Displays my favourite images on home page | Users are able to view images from available categories |
| Images on click | Users could view a specific images larger view modes|  | 
| Image links | Users are able to copy images links for download and or view on cloudinary | Users can paste links on diffrent tab to access image on cloudinary |


****
## Author

* Design and developed by: [John Kimani](https://github.com/John-Kimani)
## Dependancies
In order for you to use the content on this repo ensure you have the following:

- A computer that runs on either of the following; (Windows 7+, Linux, Mac OS)
- Python 3.6+