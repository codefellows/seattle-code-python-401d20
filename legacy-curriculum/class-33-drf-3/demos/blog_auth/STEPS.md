# Lab Steps

## Containerizing

- first, just Django
  - mind ctrl+c vs docker-compose down
- add db

## Production grade server

- gunicorn
  - https://gunicorn.org/
- whitenoise
  - http://whitenoise.evans.io/en/stable/
- django-cors-headers
  - https://github.com/adamchainz/django-cors-headers
- allowed_hosts

    ```
    CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    )
    ```


## JWT Authentication

- install `djangorestframework-simplejwt = "*"`
- add default authentication classes
- add urls
