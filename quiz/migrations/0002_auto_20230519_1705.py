# Generated by Django 3.1.4 on 2023-05-19 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertestattempt',
            name='completed_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usertestattempt',
            name='incorrect_questions',
            field=models.ManyToManyField(to='quiz.Question'),
        ),
        migrations.AlterField(
            model_name='usertestattempt',
            name='correct_answers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usertestattempt',
            name='incorrect_answers',
            field=models.IntegerField(),
        ),
    ]
