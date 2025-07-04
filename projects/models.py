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
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.owner}'

class Vacancy(models.Model):
    project = models.ForeignKey(Project, related_name='vacancies', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=VACANCY_STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.project}'