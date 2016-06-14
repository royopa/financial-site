# Flask Skeleton

Flask starter project...

[![Build Status](https://travis-ci.org/realpython/flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/flask-skeleton)

## Quick Start

### Basics

1. Activate a virtualenv
.\python3_dev\Scripts\activate.bat

2. Install the requirements
cd flask-skeleton
pip install -r requirements.txt

### Set Environment Variables

Update *config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Create DB

```sh
$ python3 manage.py create_db
$ python3 manage.py db init
$ python3 manage.py db migrate
$ python3 manage.py create_admin
$ python3 manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
