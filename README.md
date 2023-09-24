# django-dash

Bootstrap theme: https://startbootstrap.com/theme/sb-admin-2
Library: 
https://pypi.org/project/django-plotly-dash/
https://django-plotly-dash.readthedocs.io/en/latest/installation.html

## Create Database

```
CREATE DATABASE django_dash OWNER postgres;
```

## Setup the environment:
```
pip3 install pipenv
```

```
pipenv install django
```

## Activate the environment:
```
pipenv shell
```

## Starting a new django project:
```
django-admin startproject <name> .
```

## Launch Server:
```
python manage.py runserver <port>
```

## Make Changes to Models:
```
python manage.py makemigrations
```

```
python manage.py migrate
```

## Update Static Files
Do NOT add static files directly at the top level 'static' folder.
Add them to a 'static' subdirectory inside the app first and then run:

```
python manage.py collectstatic
```