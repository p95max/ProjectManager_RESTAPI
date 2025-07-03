from rest_framework import viewsets
from projects.models import Project, Vacancy
from projects.serializers import ProjectSerializer, VacancySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all().order_by('-created_at')
    serializer_class = VacancySerializer
