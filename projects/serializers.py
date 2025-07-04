from rest_framework import serializers
from projects.models import Project, Vacancy


class ProjectSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Project.

    Преобразует данные модели Project в JSON и обратно.
    Включает все поля модели для CRUD-операций.

    Attributes:
        Meta: Метаданные сериализатора, указывающие модель и поля.
    """
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True, 'max_length': 255},
        }


class VacancySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Vacancy.

    Преобразует данные модели Vacancy в JSON и обратно.
    Включает все поля модели для CRUD-операций.

    Attributes:
        Meta: Метаданные сериализатора, указывающие модель и поля.
    """
    class Meta:
        model = Vacancy
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True, 'max_length': 255},
            'project': {'required': True},
        }