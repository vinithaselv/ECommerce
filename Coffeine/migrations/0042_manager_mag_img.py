# Generated by Django 5.0.6 on 2024-09-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0041_alter_manager_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='mag_img',
            field=models.ImageField(null=True, upload_to='folder'),
        ),
    ]
