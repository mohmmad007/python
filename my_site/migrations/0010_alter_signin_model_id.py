# Generated by Django 4.1 on 2024-04-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0009_alter_signin_model_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
