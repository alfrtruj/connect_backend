# Generated by Django 3.2 on 2021-04-25 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_rename_files_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='package',
            new_name='aippackage',
        ),
    ]
