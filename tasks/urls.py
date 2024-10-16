from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('tasks/<slug>/', views.task_detail, name='task_detail'),
    # path('task/add', views.add_task, name='add-task'),
]
