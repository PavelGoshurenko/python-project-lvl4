from django.test import TestCase
from tasks.models import Tag, TaskStatus


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="test_tag")
        pass

    def setUp(self):
        pass

    def test_default_statuses(self):
        self.assertEqual(TaskStatus.objects.count(), 4)
        self.assertEqual(TaskStatus.objects.get(id=1).name, "New")

    def test_false_is_true(self):
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1 + 1, 2)
