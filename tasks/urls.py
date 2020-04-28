from django.urls import path

from tasks import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>', views.task, name='task'),
    url(r'^task/create/$', views.TaskCreate.as_view(), name='task_create'),
    url(r'^task/(?P<pk>\d+)/update/$', views.TaskUpdate.as_view(), name='task_update'),
    url(r'^task/(?P<pk>\d+)/delete/$', views.TaskDelete.as_view(), name='task_delete'),
]
