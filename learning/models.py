from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Course(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = "not_started", "Not started"
        IN_PROGRESS = "in_progress", "In progress"
        COMPLETED = "completed", "Completed"

    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.NOT_STARTED
    )
    completion_percentage = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(completion_percentage__gte=0)
                & models.Q(completion_percentage__lte=100),
                name="course_percentage_range",
            ),
            models.CheckConstraint(
                condition=models.Q(status__in=["not_started", "in_progress", "completed"]),
                name="course_valid_status",
            ),
        ]

    def __str__(self):
        return self.title
