# Generated by Django 5.0.6 on 2024-09-09 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0011_usermodel_address_usermodel_country_usermodel_dob_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='country',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='dob',
            new_name='dog',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='phonno',
            new_name='phoneno',
        ),
    ]
