from django.urls import path
from . import views

urlpatterns = [
    path('task/create/', views.task_create_or_edit, name='task_create'),  # Create Task
    path('task/<int:id>/edit/', views.task_create_or_edit, name='task_edit'),  # Edit Task
    path('task/<int:id>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:id>/mark-completed/', views.mark_task_completed, name='task_mark_completed'), 
    path('', views.task_list, name='task_list'),
]
