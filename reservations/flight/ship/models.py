from django.core.validators import MinValueValidator
from django.db import models

from reservations.flight.models import AbstractFlight
from reservations.models import AbstractReservationFlight


class Ship(AbstractFlight):
    captain = models.CharField(max_length=50)
    number_reserved = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    max_reservation = models.PositiveSmallIntegerField(default=150)

    def __str__(self):
        return self.captain


class ShipReservation(AbstractReservationFlight):
    ship = models.ForeignKey(Ship, on_delete=models.PROTECT, related_name="ship_reservation")

    def __str__(self):
        return "{} - {} -> {}".format(self.user.phone, self.ship.captain, self.check_source_date)
