# Generated by Django 3.2 on 2021-04-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0005_alter_file_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
    ]