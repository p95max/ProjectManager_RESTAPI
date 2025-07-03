from rest_framework.routers import DefaultRouter
from .views import ProjectListView

router = DefaultRouter()
router.register(r'projects', ProjectListView, basename='project')

urlpatterns = router.urls