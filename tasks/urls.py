from django.conf.urls import url
from django.urls import path
from tasks import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    path('task/<int:task_id>', views.task, name='task'),
    url(r'^task/create/$', views.TaskCreate.as_view(), name='task_create'),
    url(
        r'^task/(?P<pk>\d+)/update/$',
        views.TaskUpdate.as_view(),
        name='task_update'
        ),
    url(
        r'^task/(?P<pk>\d+)/delete/$',
        views.TaskDelete.as_view(),
        name='task_delete'
        ),
    path('tags', views.tags, name='tags'),
    path('tag/<int:tag_id>', views.tag, name='tag'),
    url(r'^tag/create/$', views.TagCreate.as_view(), name='tag_create'),
    url(
        r'^tag/(?P<pk>\d+)/update/$',
        views.TagUpdate.as_view(),
        name='tag_update'
        ),
    url(
        r'^tag/(?P<pk>\d+)/delete/$',
        views.TagDelete.as_view(),
        name='tag_delete'),
    path('task_statuses', views.task_statuses, name='task_statuses'),
    path(
        'task_status/<int:task_status_id>',
        views.task_status,
        name='task_status'
        ),
    url(
        r'^task_status/create/$',
        views.TaskStatusCreate.as_view(),
        name='task_status_create'),
    url(
        r'^task_status/(?P<pk>\d+)/update/$',
        views.TaskStatusUpdate.as_view(),
        name='task_status_update'
        ),
    url(
        r'^task_status/(?P<pk>\d+)/delete/$',
        views.TaskStatusDelete.as_view(),
        name='task_status_delete'
        ),
]
