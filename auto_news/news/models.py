from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255, unique=True)
    summary = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
