# Generated by Django 5.0.6 on 2024-09-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0018_productmodel_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='item_name',
            new_name='pro_name',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='item_no',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='status',
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
