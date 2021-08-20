from rest_framework import serializers
from .models import Book,Article,ArticleImage
import json

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class ArticleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImage
        fields = '__all__'

from django.core import serializers as django_serializers


class BookSerializer(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()

    def get_article(self, obj):
        article_data = Article.objects.filter(is_book_id=obj.id)
        return_data = django_serializers.serialize("json", article_data, ensure_ascii=False)
        return json.loads(return_data)

    class Meta:
        model = Book
        model_fields = ['id', 'thumbnail', 'title', 'description', 'created_at', 'is_public']
        extra_fields = ['article']
        fields = model_fields + extra_fields