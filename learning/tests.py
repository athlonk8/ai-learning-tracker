from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase

from .models import Course


class CourseTests(TestCase):
    def test_course_persists_with_defaults(self):
        course = Course.objects.create(title="AI Dev Tools Zoomcamp")
        saved = Course.objects.get(pk=course.pk)
        self.assertEqual(saved.title, "AI Dev Tools Zoomcamp")
        self.assertEqual(str(saved), saved.title)
        self.assertEqual(saved.status, Course.Status.NOT_STARTED)
        self.assertEqual(saved.completion_percentage, 0)

    def test_valid_statuses_and_percentage_endpoints(self):
        for status in Course.Status.values:
            for percentage in (0, 50, 100):
                with self.subTest(status=status, percentage=percentage):
                    course = Course(
                        title="AI course", status=status,
                        completion_percentage=percentage,
                    )
                    course.full_clean()
                    course.save()
                    course.refresh_from_db()
                    self.assertEqual(course.status, status)
                    self.assertEqual(course.completion_percentage, percentage)

    def test_model_validation_rejects_invalid_fields(self):
        for field, value in (
            ("title", ""), ("title", "x" * 201),
            ("status", "unknown"),
            ("completion_percentage", -1), ("completion_percentage", 101),
        ):
            with self.subTest(field=field, value=value):
                course = Course(title="AI course")
                setattr(course, field, value)
                with self.assertRaises(ValidationError) as error:
                    course.full_clean()
                self.assertIn(field, error.exception.message_dict)

    def test_database_rejects_invalid_progress_without_model_validation(self):
        course = Course.objects.create(title="AI course")
        for changes in (
            {"status": "unknown"},
            {"completion_percentage": -1},
            {"completion_percentage": 101},
        ):
            with self.subTest(changes=changes):
                with self.assertRaises(IntegrityError), transaction.atomic():
                    Course.objects.filter(pk=course.pk).update(**changes)
                course.refresh_from_db()
                self.assertEqual(course.status, Course.Status.NOT_STARTED)
                self.assertEqual(course.completion_percentage, 0)
