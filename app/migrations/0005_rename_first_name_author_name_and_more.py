# Generated by Django 4.1.4 on 2023-02-08 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]
