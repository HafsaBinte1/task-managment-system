# Generated by Django 4.2.7 on 2023-12-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('Description', models.TextField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
