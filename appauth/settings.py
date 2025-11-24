# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-v_=v&6-l*7f&$gy@(r8n3ra9*m#(9d80s*6b%sb)r5ijnt$u-+'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# # Application definition

# INSTALLED_APPS = [
#     'corsheaders',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'appusers',    
#     'rest_framework',
#     'rest_framework_simplejwt',
#     #configuração login do google
#     'rest_framework.authtoken',
#     "django.contrib.sites",
#     "rest_framework_simplejwt.token_blacklist",
#     "allauth",
#     "allauth.account",
#     "allauth.socialaccount",
#     "allauth.socialaccount.providers.google",
#     "dj_rest_auth",
#     "dj_rest_auth.registration",
#     'accounts',
# ]
# SITE_ID = 1

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # <--- TEM QUE ESTAR AQUI
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'allauth.account.middleware.AccountMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'appauth.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'appauth.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# import os
# import dj_database_url

# # Configuração Padrão (Seu MySQL Local)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'blog2',
#         'USER': 'root',
#         'PASSWORD': '1234',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }

# # Configuração de Produção (Render + Neon)
# # Se o Render fornecer a variável DATABASE_URL, usamos ela (Postgres)
# # Se não fornecer, o código acima (MySQL) continua valendo.
# database_url = os.environ.get('DATABASE_URL')

# if database_url:
#     DATABASES['default'] = dj_database_url.parse(
#         database_url,
#         conn_max_age=600,
#         conn_health_checks=True,
#         ssl_require=True,
#     )


# # Password validation
# # https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.2/topics/i18n/

# LANGUAGE_CODE = 'pt-br'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL = 'static/'

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST_FRAMEWORK = {
#     # settings.py - Sugestão de Ordem
# 'DEFAULT_AUTHENTICATION_CLASSES': (
#     'rest_framework.authentication.SessionAuthentication', # <-- DEVE SER O PRIMEIRO
#     # 'rest_framework_simplejwt.authentication.JWTAuthentication', # Remova se não estiver usando
#     # "accounts.authentication.CookieJWTAuthentication", # Remova se não estiver usando
#     'rest_framework.authentication.BasicAuthentication',
# ),
#     "DEFAULT_PERMISSION_CLASSES": (
        
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     }
# # Configuração de Autenticação com allauth
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend', # Autenticação padrão do Django
#     'allauth.account.auth_backends.AuthenticationBackend', # Autenticação do allauth
# ]

# CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173", # Exemplo para um frontend React  
#     "http://127.0.0.1:8000",  
#     "http://127.0.0.1:5173",
# ]

# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:5173",
# ]

# CORS_ALLOW_HEADERS = [
#     "content-type",
#     "x-csrftoken",
#     "accept",
#     "authorization",
# ]

# from datetime import timedelta
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15), 
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     "AUTH_COOKIE": "access",
#     "AUTH_COOKIE_HTTP_ONLY": True,
#     "AUTH_COOKIE_SECURE": False,  # True se usar HTTPS
# }

# # Configurações do allauth
# ACCOUNT_EMAIL_VERIFICATION = 'none' # Para este exemplo, não vamos verificar email
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# LOGIN_REDIRECT_URL = 'http://localhost:5173/posts' # Para onde redirecionar após o login (Frontend)
# ACCOUNT_LOGOUT_REDIRECT_URL = 'http://localhost:5173/' # Para onde redirecionar após o logout (Frontend)

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# # --- Configuração do Cookie de Sessão ---
# # O Django já usa HttpOnly por padrão, mas é bom ser explícito.
# SESSION_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SAMESITE = 'Lax' # Necessário para permitir o envio em requisições de sites diferentes (3000 -> 8000)
# SESSION_COOKIE_SECURE = False # Em produção, mude para True (requer HTTPS)
# CSRF_COOKIE_SAMESITE = 'Lax'
# CSRF_COOKIE_HTTPONLY = False # Django também protege o cookie CSRF
# CSRF_COOKIE_SECURE = False # Em produção, mude para True

# # Configurações do Google Provider
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'OAUTH_PKCE_ENABLED': True, # Recomendado para segurança
#     }
# }

# SOCIALACCOUNT_LOGIN_ON_GET = True

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

from pathlib import Path
import os
import dj_database_url
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURANÇA E AMBIENTE ---
# No Render, essa chave deve vir das variáveis de ambiente. 
# Localmente usa a 'django-insecure'
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-v_=v&6-l*7f&$gy@(r8n3ra9*m#(9d80s*6b%sb)r5ijnt$u-+')

# O Render define a variável 'RENDER' automaticamente.
# Se estiver no Render, DEBUG vira False. Se não, vira True.
IN_RENDER = os.environ.get('RENDER')
DEBUG = not IN_RENDER 

# Hosts permitidos
# Aceita o host do Render automaticamente ou '*'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')


# Application definition
INSTALLED_APPS = [
    'corsheaders', # Sempre no topo se possível
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Opcional: ajuda a testar whitenoise localmente
    'django.contrib.staticfiles',
    'appusers',    
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    "django.contrib.sites",
    "rest_framework_simplejwt.token_blacklist",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    'accounts',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # OBRIGATÓRIO SER O PRIMEIRO
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # LOGO APÓS SECURITY
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'appauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'appauth.wsgi.application'


# --- BANCO DE DADOS (HÍBRIDO) ---
# Padrão: MySQL Local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog2',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Produção: PostgreSQL (Neon)
# O Render fornece DATABASE_URL automaticamente nas variáveis de ambiente
database_url = os.environ.get('DATABASE_URL')
if database_url:
    DATABASES['default'] = dj_database_url.parse(
        database_url,
        conn_max_age=600,
        conn_health_checks=True,
        ssl_require=True,
    )


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- ARQUIVOS ESTÁTICOS ---
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- REST FRAMEWORK ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication', 
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication', # Adicionei JWT aqui caso precise
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# --- CORS E CSRF (CRÍTICO PARA FRONTEND SEPARADO) ---
CORS_ALLOW_CREDENTIALS = True

# Pega a URL do Frontend da variável de ambiente ou usa localhost
FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://localhost:5173')

CORS_ALLOWED_ORIGINS = [
    FRONTEND_URL,          # URL da Vercel (Produção)
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
]

# CSRF Trusted Origins é obrigatório para o Admin funcionar no Render
RENDER_EXTERNAL_URL = os.environ.get('RENDER_EXTERNAL_URL') # Render cria essa variável auto

CSRF_TRUSTED_ORIGINS = [
    FRONTEND_URL,
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
if RENDER_EXTERNAL_URL:
    CSRF_TRUSTED_ORIGINS.append(RENDER_EXTERNAL_URL) # Adiciona https://seu-app.onrender.com


CORS_ALLOW_HEADERS = [
    "content-type",
    "x-csrftoken",
    "accept",
    "authorization",
]


# --- JWT ---
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15), 
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    "AUTH_COOKIE": "access",
    "AUTH_COOKIE_HTTP_ONLY": True,
    "AUTH_COOKIE_SECURE": not DEBUG, # True em produção (HTTPS), False local
}


# --- ALLAUTH & REDIRECTS ---
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# Redireciona para a URL do frontend definida na variável ou localhost
LOGIN_REDIRECT_URL = f"{FRONTEND_URL}/posts"
ACCOUNT_LOGOUT_REDIRECT_URL = f"{FRONTEND_URL}/"


# --- COOKIES DE SESSÃO (PRODUÇÃO VS LOCAL) ---
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax' 
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = False 

# Em produção (Render), isso TEM que ser True por causa do HTTPS
SESSION_COOKIE_SECURE = not DEBUG 
CSRF_COOKIE_SECURE = not DEBUG


# --- GOOGLE OAUTH ---
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    }
}
SOCIALACCOUNT_LOGIN_ON_GET = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

