from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('tasks/<slug>/', views.task_detail, name='task_detail'),
    path('add/', views.add_task, name='add-task'),
    path('pending/', views.task_pending, name='task-pending'),
    path('done/', views.task_done, name='task-done'),
    path('tasks/<slug>/toggle', views.task_toggle, name='task-toggle'),
    path('tasks/<slug>/edit', views.task_edit, name='task-edit'),
    path('tasks/<slug>/delete', views.task_delete, name='task-delete'),
]
