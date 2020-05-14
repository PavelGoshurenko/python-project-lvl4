from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.TaskView.as_view(), name='task'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path(
        'task/<int:pk>/update/',
        views.TaskUpdate.as_view(),
        name='task_update'
        ),
    path(
        'task/<int:pk>/delete/',
        views.TaskDelete.as_view(),
        name='task_delete'
        ),
    path('tags/', views.TagsView.as_view(), name='tags'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create'),
    path(
        'tag/<int:pk>/update/',
        views.TagUpdate.as_view(),
        name='tag_update'
        ),
    path(
        'tag/<int:pk>/delete/',
        views.TagDelete.as_view(),
        name='tag_delete'
        ),
    path(
        'task_statuses/',
        views.TaskStatusesView.as_view(),
        name='task_statuses'
        ),
    path(
        'task_status/<int:pk>/',
        views.TaskStatusView.as_view(),
        name='task_status'
        ),
    path(
        'task_status/create/',
        views.TaskStatusCreate.as_view(),
        name='task_status_create'),
    path(
        'task_status/<int:pk>/update/',
        views.TaskStatusUpdate.as_view(),
        name='task_status_update'
        ),
    path(
        'task_status/<int:pk>/delete/',
        views.TaskStatusDelete.as_view(),
        name='task_status_delete'
        ),
]
