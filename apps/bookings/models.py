from django.db import models
from django.contrib.auth.models import User

from apps.main.models import BaseModel
from apps.tours.models import Tour


class StatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    PAYMENT_PENDING = 'PAYMENT_PENDING', 'Payment Pending'
    PAID = 'PAID', 'Paid'
    TICKET_ISSUED = 'TICKET_ISSUED', 'Ticket Issued'
    CANCELLED = 'CANCELLED', 'Cancelled'
    REFUND_REQUESTED = 'REFUND_REQUESTED', 'Refund Requested'
    REFUNDED = 'REFUNDED', 'Refunded'
    COMPLETED = 'COMPLETED', 'Completed'
    FAILED = 'FAILED', 'Failed'


class Booking(BaseModel):
    tour = models.ForeignKey(Tour, models.SET_NULL, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )
    adult_count = models.PositiveSmallIntegerField(default=1)
    kid_count = models.PositiveSmallIntegerField(default=1)
    pet_count = models.PositiveSmallIntegerField(default=1)
    total_price = models.DecimalField(decimal_places=2, default=0, max_digits=8)
    discount = models.DecimalField(decimal_places=2, default=0, max_digits=8)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
