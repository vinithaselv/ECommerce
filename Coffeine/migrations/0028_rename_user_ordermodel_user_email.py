# Generated by Django 5.0.6 on 2024-09-17 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0027_ordermodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='user',
            new_name='user_email',
        ),
    ]
