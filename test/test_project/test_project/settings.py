import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "some secret"

DEBUG = False

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "test_app",
    "pybb.apps.PybbConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "pybb.middleware.PybbMiddleware",
]

ROOT_URLCONF = "test_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "pybb.context_processors.processor",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "TEST_CHARSET": "utf8",
    }
}
test_db = os.environ.get("DB", "sqlite")
if test_db == "mysql":
    DATABASES["default"].update(
        {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "pybbm",
            # 'USER': 'root',
            "TEST_COLLATION": "utf8_general_ci",
        }
    )
elif test_db == "postgres":
    DATABASES["default"].update(
        {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            # 'USER': 'postgres',
            "NAME": "pybbm",
            "OPTIONS": {},
        }
    )


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SITE_ID = 1
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "..", "pybb_upload")
MEDIA_URL = "/media/"
AUTH_USER_MODEL = "test_app.CustomUser"
LOGIN_URL = "/"
PYBB_ATTACHMENT_ENABLE = True
PYBB_PROFILE_RELATED_NAME = "pybb_customprofile"
