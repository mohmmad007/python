# Generated by Django 4.1 on 2024-04-09 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0018_remove_suggestion_model_users_suggestion_model_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='suggestion_model',
        ),
    ]