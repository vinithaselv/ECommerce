# Generated by Django 5.0.6 on 2024-09-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0025_addtocartmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='country',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
