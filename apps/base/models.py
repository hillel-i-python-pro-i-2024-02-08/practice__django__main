from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Status(models.TextChoices):
        OPENED = "OP"
        IN_PROGRESS = "IP"
        PAUSED = "PA"
        COMPLETED = "CO"

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.OPENED,
    )