from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, VacancyViewSet

router = DefaultRouter()
"""
Роутер для настройки URL-адресов API.

Настраивает маршруты для ViewSet'ов Project и Vacancy.
Использует DefaultRouter для автоматической генерации URL.

Attributes:
    router: Экземпляр DefaultRouter для регистрации маршрутов.
"""
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'vacancies', VacancyViewSet, basename='vacancy')

urlpatterns = router.urls