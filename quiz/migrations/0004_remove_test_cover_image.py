# Generated by Django 3.1.4 on 2023-05-27 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_test_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='cover_image',
        ),
    ]
