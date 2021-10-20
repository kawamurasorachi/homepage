from django.db import models
from taggit.managers import TaggableManager


class Book(models.Model):
    thumbnail = models.ImageField(upload_to='book_thumbnail')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Article(models.Model):
    thumbnail = models.ImageField(upload_to='article_thumbnail')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    tags = TaggableManager()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    is_book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.PROTECT)
    is_public = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    image = models.ImageField(upload_to='article_image')

class Work(models.Model):
    thumbnail = models.ImageField(upload_to='work_thumbnail')
    tag = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)  
    repo_url = models.URLField(blank=True)
    site_url = models.URLField(blank=True)
