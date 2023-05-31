from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Test(models.Model):
    DIFFICULTY_EASY = 'E'
    DIFFICULTY_MEDIUM = 'M'
    DIFFICULTY_HARD = 'H'

    DIFFICULTY_CHOICES = [
        (DIFFICULTY_EASY, 'Легкая'),
        (DIFFICULTY_MEDIUM, 'Средняя'),
        (DIFFICULTY_HARD, 'Сложная'),
    ]

    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default=DIFFICULTY_EASY)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text

class UserTestAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    incorrect_questions = models.ManyToManyField(Question) # Новое поле
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()
    completed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.test.title}'
