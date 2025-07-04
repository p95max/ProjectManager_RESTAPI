from pathlib import Path
from dotenv import load_dotenv
import os

"""
Модуль настроек проекта ProjectManager.

Содержит конфигурацию Django-приложения, включая подключение к базе данных,
настройки безопасности, статических файлов и CORS.

Dependencies:
    - pathlib: Для работы с путями файлов.
    - dotenv: Для загрузки переменных окружения из .env.
    - os: Для работы с операционной системой.
"""

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
"""
Базовый каталог проекта.

Определяется как родительская директория текущего файла settings.py.
"""

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in .env")
"""
Секретный ключ проекта.

Загружается из переменной окружения SECRET_KEY, с fallback-значением для разработки.
Примечание: Fallback-значение небезопасно для продакшена.
"""

DEBUG = os.getenv('DEBUG', 'True') == 'True'
"""
Режим отладки.

True, если переменная окружения DEBUG равна 'True' (чувствительно к регистру).
"""

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if os.getenv('ALLOWED_HOSTS') else []
"""
Список разрешенных хостов.

Загружается из переменной окружения ALLOWED_HOSTS как список, разделенный запятыми.
Пустой список по умолчанию.
"""

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'projects',
]
"""
Список установленных приложений.

Включает стандартные приложения Django, а также сторонние (corsheaders, rest_framework, drf_yasg)
и собственное приложение projects.
"""

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""
Список промежуточного ПО (middleware).

Определяет порядок обработки запросов, включая CORS, безопасность и аутентификацию.
"""

ROOT_URLCONF = 'ProjectManager.urls'
"""
Модуль конфигурации URL.

Указывает основной файл маршрутов проекта (ProjectManager/urls.py).
"""

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
"""
Настройки шаблонов.

Указывает движок шаблонов Django и директории поиска (BASE_DIR / 'templates').
"""

WSGI_APPLICATION = 'ProjectManager.wsgi.application'
"""
Приложение WSGI.

Указывает точку входа для WSGI-сервера (ProjectManager/wsgi.py).
"""

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    },
}
"""
Конфигурация базы данных.

Использует PostgreSQL с параметрами, загружаемыми из переменных окружения.
"""

# Password validation
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
"""
Валидаторы паролей.

Стандартные валидаторы Django для проверки надежности паролей.
"""

# Internationalization
LANGUAGE_CODE = 'en-us'
"""
Код языка.

Установлен на 'en-us' (английский, США).
"""

TIME_ZONE = 'Europe/Berlin'
"""
Часовой пояс.

Установлен на 'Europe/Berlin' (Центральноевропейское время).
"""

USE_I18N = True
"""
Включение интернационализации.

True для поддержки перевода текста.
"""

USE_TZ = True
"""
Использование часовых поясов.

True для работы с временными зонами.
"""

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
"""
Корневая директория статических файлов.

Путь для сбора статических файлов (BASE_DIR / 'staticfiles').
"""

STATIC_URL = '/static/'
"""
URL для статических файлов.

Делает статические файлы доступными по '/static/'.
"""

# CORS settings
CORS_ALLOW_ALL_ORIGINS = os.getenv('CORS_ALLOW_ALL_ORIGINS', 'False') == 'True'
"""
Разрешение всех источников CORS.

True, если переменная окружения CORS_ALLOW_ALL_ORIGINS равна 'True'.
"""

CORS_ALLOWED_ORIGINS = [
    origin.strip() for origin in os.getenv('CORS_ALLOWED_ORIGINS', '').split(',') if origin.strip()
]
"""
Список разрешенных источников CORS.

Загружается из переменной окружения CORS_ALLOWED_ORIGINS как список, разделенный запятыми.
"""

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"""
Тип первичного ключа по умолчанию.

Установлен на BigAutoField для поддержки больших объемов данных.
"""