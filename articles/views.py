from django.shortcuts import render,redirect
from .forms import AritcleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        form = AritcleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = AritcleForm()

    context = {
        'form': form,
    }
    return render (request,'form.html',context)

def detail(request,id):
    article = Article.objects.get(id=id)

    context = {
        'article': article,
    }
    return render(request,'detail.html',context)


def comment_create(request,article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user.id = request.user.id
            comment.article.id = article_id
            comment.save()
            return redirect('articles:detail', id=article_id)
    else:
        form = CommentForm()
    
    context = {
        'form': form,
    }

    return redirect('articles:detail',id=article_id)
