import django_filters
from .models import CustomUser
from django.db import models


class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'surname']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
