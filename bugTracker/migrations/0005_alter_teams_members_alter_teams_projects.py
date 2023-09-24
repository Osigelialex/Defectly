# Generated by Django 4.2.4 on 2023-09-08 21:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugTracker', '0004_rename_created_at_project_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='members',
            field=models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teams',
            name='projects',
            field=models.ManyToManyField(related_name='teams', to='bugTracker.project'),
        ),
    ]