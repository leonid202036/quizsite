import nested_admin
from django.contrib import admin
from .models import Test, Question, Answer, UserTestAttempt

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 3  # default number of choices

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    extra = 1  # default number of questions
    inlines = [AnswerInline]

class TestAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserTestAttempt)
