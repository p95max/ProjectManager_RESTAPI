from rest_framework import viewsets
from projects.models import Project
from projects.serializers import ProjectSerializer

class ProjectListView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
