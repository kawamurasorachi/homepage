from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, Article, ArticleImage, Work
from taggit.models import Tag
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from .renderers import BookJSONRenderer, ArticleJSONRenderer, ArticleImageJSONRenderer, TagJSONRenderer, WorkJSONRenderer
from .serializers import BookSerializer, ArticleSerializer, ArticleImageSerializer, TagSerializer, WorkSerializer

from django_filters.rest_framework import DjangoFilterBackend

from .filters import ArticleFilter

class BookListApiView(ListAPIView):
    model = Book
    queryset = Book.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (BookJSONRenderer, )
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id',)

class BookUpdateApiView(UpdateAPIView):
    model = Book
    queryset = Book.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (BookJSONRenderer, )
    serializer_class = BookSerializer

class ArticleListApiView(ListAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (ArticleJSONRenderer, )
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id','is_book')

class ArticleNotBookListApiView(ListAPIView):
    model = Article
    queryset = Article.objects.filter(is_book__isnull=True)
    permission_classes = (AllowAny, )
    renderer_classes = (ArticleJSONRenderer, )
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ArticleFilter


class TagsListApiView(ListAPIView):
    model = Tag
    queryset = Tag.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (TagJSONRenderer, )
    serializer_class = TagSerializer


class WorkListApiView(ListAPIView):
    model = Work
    queryset = Work.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (WorkJSONRenderer, )
    serializer_class = WorkSerializer

class ArticleCreateApiView(CreateAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (ArticleJSONRenderer, )
    serializer_class = ArticleSerializer

class ArticleImageCreateApiView(CreateAPIView):
    model = ArticleImage
    queryset = ArticleImage.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (ArticleImageJSONRenderer, )
    serializer_class = ArticleImageSerializer


class ArticleUpdateApiView(UpdateAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (ArticleJSONRenderer, )
    serializer_class = ArticleSerializer


class BookCreateApiView(CreateAPIView):
    model = Book
    queryset = Book.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (BookJSONRenderer, )
    serializer_class = BookSerializer
