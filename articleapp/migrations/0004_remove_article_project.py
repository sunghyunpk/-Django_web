# Generated by Django 3.1.5 on 2021-02-09 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0003_article_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='project',
        ),
    ]
