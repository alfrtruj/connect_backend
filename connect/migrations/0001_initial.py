# Generated by Django 3.2 on 2021-04-23 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='uploads/images')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('package', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('filetype', models.CharField(max_length=50)),
            ],
        ),
    ]
