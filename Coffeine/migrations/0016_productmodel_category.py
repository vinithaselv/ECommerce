# Generated by Django 5.0.6 on 2024-09-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0015_productmodel_alter_categorymodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
