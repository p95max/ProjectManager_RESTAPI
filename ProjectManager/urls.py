from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="Project Manager API",
        default_version='v1',
        description="API for projects managing",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', lambda r: redirect('schema-swagger-ui')),
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
"""
Основные маршруты URL для приложения.

Включает административную панель, API-роуты и документацию.
Динамически добавляет статические файлы в режиме отладки.

Paths:
    /admin/: Административная панель Django.
    /api/: Включение маршрутов приложения projects.
    /swagger/: Интерфейс Swagger для документации API.
    /redoc/: Интерфейс ReDoc для документации API.
"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
    Динамическое добавление маршрутов для статических файлов.

    Активно только в режиме отладки (DEBUG=True).
    Использует настройки STATIC_URL и STATIC_ROOT из settings.
    """