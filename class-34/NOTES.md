# Lab Steps

## SSH

- ssh-keygen -t rsa
  - give it a name, I chose `python-401d13`
- ssh-copy-id -i python-401d13.rsa.pub root@167.172.117.35
- ssh root@167.172.117.35

## Django Environment

- pipenv install django-environ
  - No need to add to INSTALLED_APPS
- create `.env` file in same location as `settings.py`
 - **TIP** create sample .env.example
 ```
 DEBUG=on
 SECRET_KEY=your-secret-key-from-settings
 ```
  - **WARNING** add `.env` to `.gitignore`
- update `settings.py` to use values in .env


CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
]

# Don't do this, but you technically can
# CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER':env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    }
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',


    # 3rd-party apps
    'rest_framework',
    'corsheaders',

    # Local
    'posts.apps.PostsConfig',
]

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env.str('SECRET_KEY')

# False if not in os.environ
DEBUG = env('DEBUG')

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))


import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()


DEBUG=off
SECRET_KEY=%bj3%zk@(9_kwe4x%=oxx51_%=tb1p-(@&ny2(xbp(q5v-1zlg
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1,172.16.0.163


[packages]
django = "*"
djangorestframework = "*"
djangorestframework-simplejwt = "*"
psycopg2-binary = "*"
gunicorn = "*"
whitenoise = "*"
django-cors-headers = "*"
django-environ = "*"
