# Generated by Django 3.1.4 on 2023-05-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_test_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='difficulty',
            field=models.CharField(choices=[('E', 'Легкая'), ('M', 'Средняя'), ('H', 'Сложная')], default='E', max_length=1),
        ),
    ]
