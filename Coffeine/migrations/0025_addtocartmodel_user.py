# Generated by Django 5.0.6 on 2024-09-13 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0024_addtocartmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocartmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coffeine.usermodel'),
        ),
    ]
