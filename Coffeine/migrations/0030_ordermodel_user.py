# Generated by Django 5.0.6 on 2024-09-17 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0029_remove_ordermodel_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coffeine.usermodel'),
        ),
    ]
