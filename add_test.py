from django.contrib.auth.models import User
from quiz.models import Test, Question, Answer

creator = User.objects.first()  

test_data = {
    'title': "Средний уровень: Основы авиационной безопасности",
    'questions': [
        {
            'text': 'Вопрос 1',
            'answers': [
                {'text': 'Ответ 1.1', 'is_correct': True},
                {'text': 'Ответ 1.2', 'is_correct': False},
            ],
        },
        # ... остальные вопросы
    ],
}

test = Test.objects.create(title=test_data['title'], created_by=creator)

for question_data in test_data['questions']:
    question = Question.objects.create(text=question_data['text'], test=test)

    for answer_data in question_data['answers']:
        Answer.objects.create(text=answer_data['text'], is_correct=answer_data['is_correct'], question=question)
