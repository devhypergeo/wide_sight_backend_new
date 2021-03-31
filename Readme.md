# Widesight Backend
## Intro 
This is widesight backend using django latest version
Real source code : https://github.com/enricofer/wide_sight

## How to use 

- #### clone this repo
```sh
    git clone https://github.com/devhypergeo/wide_sight_backend_new.git
```
- #### install requirements 
```sh
    pip install -r requirements.txt
```

> maybe there will be a package that you have to install manually

- #### settings db
this repo using postgis (postgresql for gis), if you want to change with others you need to configure in /ws/settings.py and create database using postgis extension.
in settings.py :
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'coba_postgis',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
- #### Make Migrations
```sh
    python manage.py make migrations
```

- #### Migrate
```sh
    python manage.py  migrate
```

- #### Run Server
```sh
    python manage.py runserver
```










