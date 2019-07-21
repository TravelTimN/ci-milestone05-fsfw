import os
import dj_database_url

# using Virtual Environments
if os.path.exists("env.py"):
    import env
    DEBUG = True
else:
    DEBUG = False
    STATICFILES_STORAGE = "custom_storages.StaticStorage"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET KEY
SECRET_KEY = os.getenv("SECRET_KEY")

# ALLOWED HOSTS
ALLOWED_HOSTS = []
host = os.getenv("SITE_NAME")
if host:
    ALLOWED_HOSTS.append(host)

# APPLICATION DEFINITION
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_cleanup",
    "materializecssform",
    "accounts",
    "stats",
    "storages",
    "tickets",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "tickets.context_processors.tickets_count",
                "tickets.context_processors.tickets_last_five",
                "tickets.context_processors.get_args",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

# DATABASE
if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.parse(os.getenv("DATABASE_URL"))
    }
else:
    print("Postgres URL not found, using sqlite3 instead")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# PASSWORD VALIDATION
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

# PASSWORD RESET BACKEND
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "accounts.backends.EmailAuth"
]

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# AWS S3 Bucket
AWS_S3_OBJECT_PARAMETERS = {
    "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
    "CacheControl": "max-age=94608000",
}
AWS_STORAGE_BUCKET_NAME = "unicorn-attractor-2bn"
AWS_S3_REGION_NAME = "eu-west-1"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY= os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None

# STATIC FILES
STATICFILES_LOCATION = "static"
# STATICFILES_STORAGE = "custom_storages.StaticStorage"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# MEDIA FILES
MEDIAFILES_LOCATION = "media"
DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


# MATERIALIZE + FONT AWESOME
MATERIALIZECSS_ICON_SET = "fontawesome"

# MESSAGES TO USER
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# KILL SESSION ON CLOSE
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# STRIPE PAYMENTS
STRIPE_PUBLISHABLE = os.getenv("STRIPE_PUBLISHABLE")
STRIPE_SECRET = os.getenv("STRIPE_SECRET")

# PASSWORD RESET SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.getenv("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_PORT = 587
