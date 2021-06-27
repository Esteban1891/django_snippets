<h1 align="center"> Welcome to django-snippets! </h1>

![logo]()

## Introduction :notebook:

This repository contains all the work done for mbc.

## Table of Contents :open_file_folder:

* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Projects](#projects)
* [Author](#author)

## About

1. **python/django installation:** :black_nib:
* How to install django
* How to run a virtual environment
* How to install third party packages
* How to run current packages
* How to handle django commands


## Requirements

* Ubuntu 20.04 LTS | WSL 2 on Windows | MacOS 10.15.7
* python 3.9.1
* Django 3.1.6
* Heroku 7.52.0
* pip 21.0.1
* All programs were run on a Vagrant(ubuntu/trusty64) (Virtualbox) environment

## Installation

![icon]()

In your terminal, git clone the directory with the following command:

```sh
git clone https://github.com/Esteban1891/django_snippets/
```

#### Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv env`
4. Activate the virtual environment by running `source env/bin/activate`

- On Windows use `source env\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

* Also you can only use `source env/bin/activate`

6. Run docker to mysql db `docker-compose up`
* To stop use `docker-compose stop`

7. Migrate existing db tables by running `python manage.py migrate`

8. Run the django collectstatic `python manage.py collectstatic`

9. Run the django development server using `python manage.py runserver`

## Usage

If you want you can use the automated or manual scripts with the above indications

```sh
./[executable.sh]
```

## Information to admin django
```python
python manage.py createsuperuser
```
| user | password | Description |
| ----- | ----- | ------ |
| esteban | esteban1891 | Admin |


## Installation on Heroku with Python

Make sure you have Python 3.9 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup)

## Have complete repository

```bash
heroku login

heroku git:clone -a esteban-django-snippets
git push heroku master

heroku run python manage.py migrate

heroku open
```

## Add Change Heroku

```bash
heroku login

cd backend/

git init

heroku git:remote -a esteban-django-snippets

git add --all

git commit -am "make it better"

git push heroku master

heroku run python manage.py migrate

heroku run python manage.py createsuperuser

heroku open
```

## Deploying to Heroku

```bash
heroku create

git push heroku master

heroku run python manage.py migrate

heroku run python manage.py createsuperuser

heroku open
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

## Author 

[Esteban De La Hoz](https://www.linkedin.com/in/esteban-de-la-hoz-romero-b6270017b/) | [Twitter](https://twitter.com/Esteban18911) | [GitHub](https://github.com/Esteban18911)
