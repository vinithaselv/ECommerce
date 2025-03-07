# Generated by Django 5.0.6 on 2024-09-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeine', '0033_ordermodel_username_alter_ordermodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='username',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='uemail',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='user_email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='payment',
            field=models.TextField(choices=[('credit_card', 'Credit Card'), ('cash', 'Cash On Delivery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
