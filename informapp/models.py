from django.db import models

# Create your models here.

class Inform(models.Model):
    text = models.CharField(max_length=255, null=False)
    #image = models.ImageField(upload_to='infrom/', null=False)
