from rest_framework import viewsets
from projects.models import Project, Vacancy
from projects.serializers import ProjectSerializer, VacancySerializer
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления проектами.

    Предоставляет CRUD-операции для модели Project.
    Сортировка по умолчанию: по убыванию даты создания (created_at).
    Требуется аутентификация пользователя.

    Attributes:
        queryset: Все объекты Project, отсортированные по created_at.
        serializer_class: Сериализатор для Project.
        permission_classes: Разрешения для доступа (только аутентифицированные пользователи).
    """
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class VacancyViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления вакансиями.

    Предоставляет CRUD-операции для модели Vacancy.
    Сортировка по умолчанию: по убыванию даты создания (created_at).
    Требуется аутентификация пользователя.

    Attributes:
        queryset: Все объекты Vacancy, отсортированные по created_at.
        serializer_class: Сериализатор для Vacancy.
        permission_classes: Разрешения для доступа (только аутентифицированные пользователи).
    """
    queryset = Vacancy.objects.all().order_by('-created_at')
    serializer_class = VacancySerializer
    permission_classes = [IsAuthenticated]
