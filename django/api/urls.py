from django.urls import path, include
from .views import (
    BookListApiView,
    BookUpdateApiView,
    BookCreateApiView,
    ArticleListApiView,
    ArticleCreateApiView,
    ArticleImageCreateApiView,
    ArticleUpdateApiView,
    ArticleNotBookListApiView,
    TagsListApiView
)


urlpatterns = [
    path('get_book/', BookListApiView.as_view()),
    path('get_article/', ArticleListApiView.as_view()),
    path('get_article_not_book/', ArticleNotBookListApiView.as_view()),
    path('get_tags/', TagsListApiView.as_view()),
    path('post_book/', BookCreateApiView.as_view()),
    path('update_book/<int:pk>', BookUpdateApiView.as_view()),
    path('post_article/', ArticleCreateApiView.as_view()),
    path('post_article_image/', ArticleImageCreateApiView.as_view()),
    path('update_article/<int:pk>', ArticleUpdateApiView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]