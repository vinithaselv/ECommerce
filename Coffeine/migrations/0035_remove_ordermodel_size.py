# Generated by Django 5.0.6 on 2024-09-17 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0034_rename_username_ordermodel_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='size',
        ),
    ]
