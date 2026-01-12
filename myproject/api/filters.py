import django_filters
from mainapp.models import TaskModel, UserModel

class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter()
    priority = django_filters.NumberFilter()
    groupby = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = TaskModel
        fields = ['completed', 'priority', 'groupby']