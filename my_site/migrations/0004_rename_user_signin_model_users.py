# Generated by Django 4.1 on 2024-04-05 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0003_rename_users_signin_model_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin_model',
            old_name='user',
            new_name='users',
        ),
    ]
