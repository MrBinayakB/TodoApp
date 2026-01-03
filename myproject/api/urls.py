from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('tasks/',views.task_list),
    path('tasks/<int:pk>',views.tasks_detail),

    path('users/',views.user_list),
    path('users/<int:pk>',views.users_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
