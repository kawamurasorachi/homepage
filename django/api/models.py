from django.db import models

# Create your models here.

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
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    is_book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.PROTECT)
    is_public = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    image = models.ImageField(upload_to='article_image')


