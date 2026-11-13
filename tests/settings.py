SECRET_KEY = "DUMMY_SECRET_KEY"  # noqa: S105

# Application definition

PROJECT_APPS = ["tests", "filters"]


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django_filters",
    *PROJECT_APPS,
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
