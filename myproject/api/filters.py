import django_filters
from mainapp.models import TaskModel, UserModel

class TaskFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    completed = django_filters.BooleanFilter()
    priority = django_filters.NumberFilter()
    groupby = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TaskModel
        fields = ['completed', 'priority', 'groupby','id']

class UserFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserModel
        fields = ['name','id','email']