from django.test import TestCase
from django.urls import reverse
from tasks.models import Tag, Task, TaskStatus


class PreinstalledDataTest(TestCase):

    def test_default_statuses(self):
        self.assertEqual(TaskStatus.objects.count(), 4)
        self.assertEqual(TaskStatus.objects.get(id=1).name, "New")


class UrlsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="test_tag")
        task_status = TaskStatus.objects.create(name="test_status")
        Task.objects.create(
            name="test_task",
            content="test_content",
            status=task_status)

    def test_get_tag_url(self):
        test_tag = Tag.objects.get(id=1)
        self.assertEquals(test_tag.get_absolute_url(), '/tasks/tag/1')

    def test_get_status_url(self):
        test_status = TaskStatus.objects.get(id=5)
        self.assertEquals(
            test_status.get_absolute_url(),
            '/tasks/task_status/5'
            )

    def test_get_task_url(self):
        test_task = Task.objects.get(id=1)
        self.assertEquals(test_task.get_absolute_url(), '/tasks/task/1')


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        TaskStatus.objects.create(name="test_status")
        # Create 10 tasks with different statuses
        number_of_tasks = 10
        status1 = TaskStatus.objects.get(name="New")
        status2 = TaskStatus.objects.get(name="Completed")
        for task_num in range(number_of_tasks):
            current_status = status1 if task_num < 3 else status2
            Task.objects.create(
                name="test_task %s" % task_num,
                content="test_content",
                status=current_status
                )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/tasks/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertTemplateUsed(resp, 'index.html')

    def test_all_task_is_ten(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['task_list']), 10)

    def test_status_filter(self):
        resp = self.client.get(reverse('index')+'?status__name=New')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['task_list']), 3)
        resp = self.client.get(reverse('index')+'?status__name=Completed')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['task_list']), 7)
