# Generated by Django 5.0.6 on 2024-09-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0021_rename_category_categorymodel_cat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
