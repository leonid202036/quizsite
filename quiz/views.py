from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Test, UserTestAttempt, Answer

# ...
@login_required
def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == "POST":
        correct_answers = 0
        incorrect_answers = 0
        incorrect_questions = []

        for question in test.questions.all():
            answer = request.POST.get(str(question.pk))

            if answer is not None and question.answers.filter(pk=answer, is_correct=True).exists():
                correct_answers += 1
            else:
                incorrect_answers += 1
                incorrect_questions.append(question)

        attempt = UserTestAttempt(
            user=request.user,
            test=test,
            correct_answers=correct_answers,
            incorrect_answers=incorrect_answers,
        )
        print(attempt)
        attempt.save()
        
        for question in incorrect_questions:
            attempt.incorrect_questions.add(question)
        attempt.save()

        return redirect('quiz:test_result', pk=attempt.pk)

    return render(request, 'quiz/test_detail.html', {'test': test})




def test_list(request):
    tests = Test.objects.all()

    return render(request, 'quiz/test_list.html', {'tests': tests})


def test_result(request, pk):
    attempt = get_object_or_404(UserTestAttempt, pk=pk)
    return render(request, 'quiz/test_result.html', {'attempt': attempt})

def statistics(request):
    attempts = UserTestAttempt.objects.filter(user=request.user).order_by('-completed_at')
    return render(request, 'quiz/statistics.html', {'attempts': attempts})