from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, Article, ArticleImage

from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from .renderers import BookJSONRenderer, ArticleJSONRenderer, ArticleImageJSONRenderer
from .serializers import BookSerializer, ArticleSerializer, ArticleImageSerializer

from django_filters.rest_framework import DjangoFilterBackend



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
    filterset_fields = ('id',)

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
