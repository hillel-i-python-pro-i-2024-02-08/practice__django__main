from django.urls import path

from apps.base import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('edit/<int:task_id>', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
]
