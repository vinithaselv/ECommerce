# Generated by Django 5.0.6 on 2024-08-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.PositiveIntegerField()),
                ('item_name', models.TextField()),
                ('pro_img', models.ImageField(null=True, upload_to='folder')),
                ('price', models.TextField()),
                ('status', models.TextField()),
            ],
        ),
    ]
