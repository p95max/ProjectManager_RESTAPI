from django.db import models

PROJECT_STATUS_CHOICES = [
    ('active', 'Active'),
    ('passed', 'Passed'),
]

VACANCY_STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
]

class Project(models.Model):
    """
    Модель для представления проекта.

    Хранит информацию о проекте, включая название, описание, владельца и статус.
    Используется для управления проектами в системе.

    Attributes:
        name (CharField): Название проекта (до 255 символов).
        description (TextField): Описание проекта (может быть пустым).
        owner (CharField): Владелец проекта (до 255 символов, может быть пустым).
        status (CharField): Статус проекта (active или passed, по умолчанию active).
        created_at (DateTimeField): Дата и время создания проекта (автоматически устанавливается).

    Methods:
        __str__: Возвращает строковое представление проекта.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.owner}'


class Vacancy(models.Model):
    """
    Модель для представления вакансии.

    Хранит информацию о вакансии, связанной с проектом, включая название, описание,
    опыт и статус. Связана с моделью Project через ForeignKey.

    Attributes:
        project (ForeignKey): Связанный проект (обязательное поле).
        name (CharField): Название вакансии (до 255 символов).
        description (TextField): Описание вакансии (может быть пустым).
        experience (CharField): Требуемый опыт (до 100 символов, может быть пустым).
        owner (CharField): Владелец вакансии (до 255 символов, может быть пустым).
        status (CharField): Статус вакансии (open или closed, по умолчанию open).
        created_at (DateTimeField): Дата и время создания вакансии (автоматически устанавливается).

    Methods:
        __str__: Возвращает строковое представление вакансии.
    """
    project = models.ForeignKey(Project, related_name='vacancies', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=VACANCY_STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.project}'