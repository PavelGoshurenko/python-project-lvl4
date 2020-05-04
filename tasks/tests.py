from django.test import TestCase
from tasks.models import Tag, TaskStatus, Task


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Tag.objects.create(name="test_tag")

        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_default_statuses(self):
        self.assertEqual(TaskStatus.objects.count(), 4)
        self.assertEqual(TaskStatus.objects.get(id=1).name, "New")

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
