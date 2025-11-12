from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url="accounts:login")
def create_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news:news_list")
    else:
        form = NewsForm()
    return render(request, "news/news_form.html", {"form" : form})

def news_list(request):
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news" : news})

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "news/news_detail.html", {"news" : news})

@user_passes_test(is_admin, login_url="accounts:login")
def update_news(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect("news:news_list")
    else:
        form = NewsForm(instance=news)
    return render(request, "news/news_form.html", {"form" : form})

@user_passes_test(is_admin, login_url="accounts:login")
def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == "POST":
        news.delete()
        return redirect("news:news_list")
    return render(request, "news/news_confirm_delete.html", {"news" : news})