from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, VacancyViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'vacancies', VacancyViewSet, basename='vacancy')

urlpatterns = router.urls