from django.db import models


class StayStatus(models.TextChoices):
    FREE = "FREE"
    SPACE = "SPACE"
    FULL = "FULL"
    CANCELLED = "CANCELLED"


class AbstractResidence(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    residence_status = models.CharField(max_length=15, choices=StayStatus.choices, default=StayStatus.FREE)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
