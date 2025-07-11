from django.contrib import admin
from .models import Project, Vacancy

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'status', 'created_at')
    search_fields = ('name', 'owner')
    list_filter = ('status', 'created_at')

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'project', 'owner', 'status', 'created_at')
    search_fields = ('name', 'owner', 'project__name')
    list_filter = ('status', 'created_at', 'project')