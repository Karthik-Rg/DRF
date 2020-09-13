import django_filters

from django.db.models import Q
from .models import Post
from django.contrib.auth.models import User

class PostFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='custom_filter')
    class Meta:
        model = Post
        fields = ['q']


    def custom_filter(self, queryset, name, value):
        return Post.objects.filter(
            Q(title__icontains=value) | Q(content__icontains=value)
        )
