from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('tasks/<slug>/', views.task_detail, name='task_detail'),
    path('add/', views.add_task, name='add-task'),
    path('pending/', views.toggle, name='task-pending'),
    path('done/', views.toggle, name='task-done'),
    path('tasks/<slug>/toggle', views.toggle, name='task-toggle'),
    path('tasks/<slug>/edit', views.toggle, name='task-edit'),
    path('tasks/<slug>/delete', views.toggle, name='task-delete'),
]
