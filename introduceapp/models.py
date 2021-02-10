from django.db import models

# Create your models here.

class Introduce(models.Model):
    image = models.ImageField(upload_to='introduce/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)
