import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xul7#nwn+^ha$!f*uq59^(88)@#v11=@1h-4%bc^dp0%@*xeoh'

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    'softpalm-store.onrender.com',
    '.onrender.com',
    '127.0.0.1',
    'localhost'
]

# ========================
# CLOUDINARY (صح)
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cloudinary',
    'cloudinary_storage',

    'accounts',
    'products',
    'cart',
    'orders',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dn0fja5vs',
    'API_KEY': '321471359398461',
    'API_SECRET': 'Pc3_p9hBnceyNlEn4osbiY4g9AI',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ========================
# STATIC (Render)
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise فقط للـ static
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ========================
# MEDIA (لا تستخدم local مع Cloudinary)
# ========================
MEDIA_URL = '/media/'
