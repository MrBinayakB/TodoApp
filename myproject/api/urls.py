from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.task_list),
    path('tasks/<int:pk>',views.tasks_detail),

    path('users/',views.user_list),
    path('users/<int:pk>',views.users_detail),
]
