# Generated by Django 5.0.6 on 2024-09-09 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0013_rename_dog_usermodel_dor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='dor',
        ),
    ]
