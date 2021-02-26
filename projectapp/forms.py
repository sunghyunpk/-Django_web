from django.forms import ModelForm

from projectapp.models import Project

class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'image2',  'title', 'description', 'title2', 'description2']
