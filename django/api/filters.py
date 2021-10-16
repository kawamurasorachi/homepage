import django_filters
from django_filters.views import FilterView
from .models import Article
from taggit.forms import TagField

class TagFilter(django_filters.CharFilter):
    field_class = TagField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)


class ArticleFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    is_book = django_filters.NumberFilter()
    tags = TagFilter(field_name='tags__slug')

    class Meta:
        model = Article
        fields=[]