# Class 33 Snippets

## Dang it all! The code got all jumbled up. Go through your API files and find the right spot for these snippets

```python
'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
]
```

```toml
python = "~3.8"
django = "^3.0.7"
djangorestframework = "^3.11.0"
gunicorn = "^20.0.4"
whitenoise = "^5.1.0"
django-cors-headers = "^3.4.0"
psycopg2-binary = "^2.8.5"
djangorestframework-simplejwt = "^4.4.0"
```

```python
from rest_framework_simplejwt import views as jwt_views
```

```python
path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
```

```docker
command: gunicorn blog_project.wsgi:application --bind 0.0.0.0:8000
```

```python
'django.contrib.sessions.middleware.SessionMiddleware',
'whitenoise.middleware.WhiteNoiseMiddleware',
'django.middleware.common.CommonMiddleware',
```

```python
'django.contrib.messages',
'whitenoise.runserver_nostatic',
'django.contrib.staticfiles',
```

```python
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
```

```yml
    volumes:
        - postgres_data:/var/lib/postgresql/data/

volumes:
    postgres_data:
```
