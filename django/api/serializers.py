from rest_framework import serializers
from .models import Book,Article,ArticleImage
import json
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from taggit.models import Tag

class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta:
        model = Article
        fields = [
            'id',
            'thumbnail',
            'title',
            'description',
            'tags',
            'content',
            'created_at',
            'is_book',
            'is_public',
        ]
    
    def get_thumbnail(self, obj):
        return '/django-media/'+str(obj.thumbnail)

    

class ArticleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImage
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

from django.core import serializers as django_serializers


class BookSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()

    def get_article(self, obj):
        article_data = Article.objects.filter(is_book_id=obj.id)
        return_data = django_serializers.serialize("json", article_data, ensure_ascii=False)
        return json.loads(return_data)

    def get_thumbnail(self, obj):
        return '/django-media/'+str(obj.thumbnail)

    class Meta:
        model = Book
        model_fields = ['id', 'thumbnail', 'title', 'description', 'created_at', 'is_public']
        extra_fields = ['article']
        fields = model_fields + extra_fields