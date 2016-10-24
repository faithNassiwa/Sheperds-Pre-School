"""
Django settings for Sheperds project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-)=vzzr9hc6_4^v(5w9_s^=5c3bs%(3@v5dlx9v)ixq4#q)*3l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_HOST_USER = 'faithnassiwa@gmail.com'  # this is my email address, use yours
EMAIL_HOST_PASSWORD = ''#app specfic password generated from support.google.com/accounts/answer/185833

ADMINS = (
    ('Faith Nassiwa', 'faithnassiwa@gmail.com'),   # email will be sent to your_email
    ('Faith Ashaba', 'faithashaba@gmail.com'),   # email will be sent to your_email
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'website',
    'admission'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Sheperds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
                'admin_tools.template_loaders.Loader',
                
            ]
        },
    },
]

WSGI_APPLICATION = 'Sheperds.wsgi.application'

ADMIN_TOOLS_THEMING_CSS = 'css/theming.css'


#To tell django-admin-tools to use your custom menu depending on the admin site being used
ADMIN_TOOLS_MENU = {
    'django.contrib.admin.site': 'django_admin_menu.CustomMenu',
    #'ispecial.admin.admin_site': 'ispecial.my_admin_menu.CustomMenu',
}

#To tell django-admin-tools to use your custom dashboards depending on the admin site being used
ADMIN_TOOLS_INDEX_DASHBOARD = {
    'django.contrib.admin.site': 'django_admin_dashboard.CustomIndexDashboard',
    #'ispecial.admin.admin_site': 'ispecial.my_admin_dashboard.CustomIndexDashboard',
}

ADMIN_TOOLS_APP_INDEX_DASHBOARD = {
    'django.contrib.admin.site': 'django_admin_dashboard.CustomIndexDashboard',
    #'ispecial.admin.admin_site': 'ispecial.my_admin_dashboard.CustomIndexDashboard',
}



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dmnqimumac8ga',
        'USER': 'nldvtzpiuxbgfb',
        'PASSWORD': 'qpVyfoEvk4bxpiz73TqA6nYXN6',
        'HOST': 'ec2-23-23-76-90.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Allow all host headers
#ALLOWED_HOSTS = ['sheperdspreschool.herokuapp.com', 'localhost']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'

#STATICFILES_DIRS = (
    #os.path.join(PROJECT_ROOT, 'static'),
#)



# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
