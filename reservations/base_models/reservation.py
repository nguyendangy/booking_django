import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from rest_framework import exceptions


class ReservedStatus(models.TextChoices):
    INITIAL = "INITIAL"
    RESERVED = "RESERVED"
    CANCELLED = "CANCELLED"
    FINISHED = "FINISHED"
    PROBLEM = "PROBLEM"


class AbstractReservation(models.Model):
    reserved_key = models.UUIDField(editable=False, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(app_label)s_%(class)s')
    adult_count = models.PositiveSmallIntegerField(default=0)
    children_count = models.PositiveSmallIntegerField(default=0)
    reserved_status = models.CharField(max_length=15, choices=ReservedStatus.choices, default=ReservedStatus.INITIAL)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractReservationResidence(AbstractReservation):
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def check_date(self):
        return self.check_out_date > self.check_in_date >= timezone.now().date()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.check_date():
            return super().save(force_insert, force_update, using, update_fields)
        raise exceptions.ValidationError("invalid dates")

    class Meta:
        abstract = True
