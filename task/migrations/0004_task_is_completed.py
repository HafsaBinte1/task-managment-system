# Generated by Django 4.2.7 on 2023-12-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]