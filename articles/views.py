from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from django.shortcuts import render, redirect
from .forms import CommentForm
from django.contrib import messages

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})



def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.order_by('-created_at')
   
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Вы должны быть авторизованы, чтобы оставить комментарий.')
            return redirect('accounts:register') # or the name of your login view
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создаем объект Comment, но пока не сохраняем в базу
            new_comment = comment_form.save(commit=False)
            # Привязываем комментарий к текущей статье
            new_comment.article = article
            # Привязываем комментарий к текущему пользователю
            new_comment.author = request.user
            # Теперь можно сохранить комментарий в базу
            new_comment.save()
    else:
        comment_form = CommentForm()

    

    return render(request, 'articles/article_detail.html', {'article': article, 'comments': comments, 'comment_form': comment_form})
