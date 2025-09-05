from django.shortcuts import render, redirect
from .models import NewsArticle
from .utils import fetch_and_store_news

def dashboard(request):
    articles = NewsArticle.objects.order_by("-published_at")
    return render(request, "news/dashboard.html", {"articles": articles})

def fetch_news_view(request):
    fetch_and_store_news()
    return redirect("dashboard")
