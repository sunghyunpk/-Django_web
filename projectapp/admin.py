from django.contrib import admin

# Register your models here.
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('image','image2', 'title', 'description', 'title2', 'description2')

admin.site.register(Project, ProjectAdmin)